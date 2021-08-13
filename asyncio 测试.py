import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


def func(sleep):
    print(f"{sleep = }")
    time.sleep(sleep)
    print(f"结束 {sleep}")

async def async_func(sleep):
    print(f"{sleep = }")
    await asyncio.sleep(sleep)
    print(f"结束 {sleep}")
    return sleep
    # async with lock:
    #     print(f"{sleep = }")
    #     await asyncio.sleep(sleep)
    #     print(f"结束 {sleep}")
    #     return sleep


async def async_thread_pool_func(func, sleep, loop):
    return await loop.run_in_executor(None, func, sleep)

def back(res):
    if res.result() == 9:
        loop.stop()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    loop = asyncio.new_event_loop()
    loop.set_default_executor(pool)
    pool.submit(start_loop, loop)
    lock = asyncio.Lock(loop=loop) # 锁 同步执行
    for i in range(10):
        # asyncio.run_coroutine_threadsafe(async_thread_pool_func(func, i, loop),loop)
        futures = asyncio.run_coroutine_threadsafe(async_func(i),loop)
        futures.add_done_callback(back)
