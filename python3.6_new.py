# 格式化字符串变量.
import asyncio

name = "lizhenbin"
# print(f'hello {name}')

# 数字变量使用下划线.
a = 1_000_000
b = 0x_FF_FF_FF
# print(a,b)
# print("{:_}".format(1000000))
# print("{:,}".format(1000000))
# print("{:_x}".format(0xFFFFFFF))

# 给变量添加注释的语法

from typing import List, Dict

a : List[int] = [1]
b : List[int] = ["bbb"]
c : List[int] #
d : Dict[str, int] = {"a":1}


# 异步生成器
async def test():
    for i in range(5):
        yield i
        await asyncio.sleep(2)

async def main():
    res = test()
    # async for i in res:
    #     print(i)
    # else: # optional
    #     print("end")
    # or
    b = await res.__anext__()
    return b

# 1
# tasks = [main()]
# asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))

# 2
# asyncio.get_event_loop().run_until_complete(main())

# 3
# asyncio.get_event_loop().run_until_complete(asyncio.gather(main()))


# 异步推导
async def test_1():
    task = [await main() for i in range(5)]
    print(task)

# asyncio.get_event_loop().run_until_complete(test_1())


# pathlib 新的路径 协议
import pathlib

path = pathlib.Path.cwd()
print(path)
print(type(path))
