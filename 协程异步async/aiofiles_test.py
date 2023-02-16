import asyncio
import aiofiles


async def write_demo():
    # 异步方式执行with操作,修改为 async with
    async with aiofiles.open("text.txt", "a", encoding="utf-8") as fp:
        await fp.write("hello world ")
        print("数据写入成功")


async def read_demo():
    async with aiofiles.open("text.txt", "r", encoding="utf-8") as fp:
        content = await fp.read()
        print(content)


async def read2_demo():
    async with aiofiles.open("text.txt", "r", encoding="utf-8") as fp:
        # 读取每行
        async for line in fp:
            print(line)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = []
    task.append(write_demo())
    task.append(read_demo())
    task.append(read2_demo())
    loop.run_until_complete(asyncio.wait(task))
