import asyncio
import os
import threading
import time
from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query
import uvicorn
from anyio.lowlevel import RunVar
from anyio import CapacityLimiter

global_request_counter = 0


# https://yanbin.blog/test-compaire-flask-fastapi-tomcat-concurrency/

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("start")
    RunVar("_default_thread_limiter").set(CapacityLimiter(5000))
    yield


app = FastAPI(lifespan=lifespan)


# @app.get("/")
# async def index(request_id: str = Query(..., alias="id")):
#     global global_request_counter
#     global_request_counter += 1
#     thread_name = threading.current_thread().name
#     thread_id = threading.current_thread().native_id
#     active_count = threading.active_count()
#     print(
#         f"{datetime.now()} - {os.getpid()}-{thread_name}-{thread_id}-{active_count}: #{global_request_counter} processing request id[{request_id}], sleeping...")
#     time.sleep(800)
#     print(f"{datetime.now()} - {os.getpid()}-{thread_name}-{thread_id}-{active_count}: done request id[{request_id}]")
#     return "hello"


async def foo(request_id):
    value = await asyncio.sleep(5, result=f'hello #{request_id}')
    return value


@app.get("/")
async def index(request_id: str = Query(..., alias="id")):
    global global_request_counter
    global_request_counter += 1
    thread_name = threading.current_thread().name
    thread_id = threading.current_thread().native_id
    active_count = threading.active_count()
    print(
        f"{datetime.now()} - {os.getpid()}-{thread_name}-{thread_id}-{active_count}: #{global_request_counter} processing request id[{request_id}], sleeping...")
    res = await foo(request_id)
    print(f"{datetime.now()} - {os.getpid()}-{thread_name}-{thread_id}-{active_count}: done request id[{request_id}]")
    return res


@app.get("/index")
def index():
    thread_id = threading.current_thread().native_id
    print(thread_id)
    print(threading.current_thread().ident)
    time.sleep(10)
    return "你好"


# 或者用命令方式启动 uvicorn app:app --host 0.0.0.0 --port 8080
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
    # uvicorn.run("fastapi_demo:app", host="0.0.0.0", port=8080, workers=2)
