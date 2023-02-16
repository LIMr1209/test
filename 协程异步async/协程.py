import asyncio
from concurrent.futures import ThreadPoolExecutor


async def async_func(sleep, lock):
    print(f"{sleep = }")
    await asyncio.sleep(sleep)
    print(f"结束 {sleep}")
    return sleep
    # async with lock:
    #     print(f"{sleep = }")
    #     await asyncio.sleep(sleep)
    #     print(f"结束 {sleep}")
    #     return sleep


async def main():
    tasks = []
    for i in range(10):
        tasks.append(async_func(2, lock))
    await asyncio.gather(*tasks)
    # await asyncio.wait(tasks)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    loop = asyncio.new_event_loop()
    loop.set_default_executor(pool)
    lock = asyncio.Lock(loop=loop)  # 锁 同步执行
    loop.run_until_complete(main())
    loop.close()
    print(222)
