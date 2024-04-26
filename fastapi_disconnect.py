"""One solution: Use a decorator to poll for the disconnect"""

import asyncio
import ctypes
import threading
import time

from asyncer import asyncify
from functools import wraps
from typing import Any, Awaitable, Callable

import uvicorn
from fastapi import FastAPI, Query, Request, HTTPException

app = FastAPI(title="Disconnect example")


async def disconnect_poller(request: Request, result: Any):
    """
    Poll for a disconnect.
    If the request disconnects, stop polling and return.
    """
    try:
        while not await request.is_disconnected():
            await asyncio.sleep(0.01)

        print("Request disconnected")

        return result
    except asyncio.CancelledError:
        print("Stopping polling loop")


def cancel_on_disconnect(handler: Callable[[Request], Awaitable[Any]]):
    """
    Decorator that will check if the client disconnects,
    and cancel the task if required.
    """

    @wraps(handler)
    async def cancel_on_disconnect_decorator(request: Request, *args, **kwargs):
        sentinel = object()

        # Create two tasks, one to poll the request and check if the
        # client disconnected, and another which is the request handler
        poller_task = asyncio.ensure_future(disconnect_poller(request, sentinel))
        handler_task = asyncio.ensure_future(handler(request, *args, **kwargs))

        done, pending = await asyncio.wait(
            [poller_task, handler_task], return_when=asyncio.FIRST_COMPLETED
        )

        # Cancel any outstanding tasks
        for t in pending:
            t.cancel()

            try:
                await t
            except asyncio.CancelledError:
                print(f"{t} was cancelled")
            except Exception as exc:
                print(f"{t} raised {exc} when being cancelled")

        # Return the result if the handler finished first
        if handler_task in done:
            return await handler_task
        if hasattr(request, "thread_id"):
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(request.thread_id),
                                                       ctypes.py_object(SystemExit))
        # Otherwise, raise an exception
        # This is not exactly needed, but it will prevent
        # validation errors if your request handler is supposed
        # to return something.
        print("Raising an HTTP error because I was disconnected!!")

        raise HTTPException(503)

    return cancel_on_disconnect_decorator


def do_sync_work(request: Request):
    request.thread_id = threading.get_ident()
    for i in range(10):
        time.sleep(1)
        print(f"Hello, {str(i)}")


@app.get("/example")
@cancel_on_disconnect
async def example(
        request: Request,
        # wait: float = Query(..., description="Tim to wait, in seconds"),
):

    try:
        # await asyncio.sleep(5)
        await asyncify(do_sync_work, cancellable=True)(request=request)
        return f"I waited for {5:.2f}s and now this is the result"
    except asyncio.CancelledError:
        print("Exiting on cancellation")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
