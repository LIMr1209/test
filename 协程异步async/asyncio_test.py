# python3.5 修改
# @asyncio.coroutine -> async
#
# yield from -> await
"""
1.事件循环

管理所有的事件，在整个程序运行过程中不断循环执行并追踪事件发生的顺序将它们放在队列中，空闲时调用相应的事件处理者来处理这些事件。

2.Future

Future对象表示尚未完成的计算，还未完成的结果

3.Task

是Future的子类，作用是在运行某个任务的同时可以并发的运行多个任务。

asyncio.Task用于实现协作式多任务的库，且Task对象不能用户手动实例化，通过下面2个函数创建：

asyncio.async()

loop.create_task() 或 asyncio.ensure_future() 或者 asyncio.create_task()
"""

# 最简单的异步IO示例
# run_until_complete():
#
# 阻塞调用，直到协程运行结束才返回。参数是future，传入协程对象时内部会自动变为future
#
# asyncio.sleep():
#
# 模拟IO操作，这样的休眠不会阻塞事件循环，前面加上await后会把控制权交给主事件循环，在休眠（IO操作）结束后恢复这个协程。
#
# 提示：若在协程中需要有延时操作，应该使用 await asyncio.sleep()，而不是使用time.sleep()，因为使用time.sleep()后会释放GIL，阻塞整个主线程，从而阻塞整个事件循环。

import asyncio
import time


async def coroutine_example(name):
    await asyncio.sleep(1)
    print(f"hello world! {name}")
    return name


# asyncio.get_event_loop().run_until_complete(coroutine_example("lizhenbin")) #python 3.6
# asyncio.run(coroutine_example("lizhenbin")) # python3.7

# 手动获取返回值
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine_example("xixi"), loop=loop)
# task = loop.create_task(coroutine_example("xixi"))
# print('运行情况：', task)
# loop.run_until_complete(task)
# print('再看下运行情况：', task)
# print("返回值",task.result())
# loop.close()

# 添加回调函数
def my_callback(future):
    print('返回值：', future.result())


#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine_example("xixi"))
# task.add_done_callback(my_callback)
# loop.run_until_complete(task)
# loop.close()

# 通过asyncio.wait()可以控制多任务
#
# asyncio.wait()是一个协程，不会阻塞，立即返回，返回的是协程对象。传入的参数是future或协程构成的可迭代对象。最后将返回值传给run_until_complete()加入事件循环

# tasks = [coroutine_example('Zarten_' + str(i)) for i in range(3)]
# wait_coro = asyncio.wait(tasks)
# asyncio.run(wait_coro)

# loop = asyncio.get_event_loop()
# tasks = []
# for i in range(3):
#     # task = asyncio.ensure_future(coroutine_example('Zarten_' + str(i)), loop=loop)
#     task = loop.create_task(coroutine_example('Zarten_' + str(i)))
#     task.add_done_callback(my_callback)
#     tasks.append(task)
#
# wait_coro = asyncio.wait(tasks)
# loop.run_until_complete(wait_coro)


async def main():
    task = asyncio.ensure_future(coroutine_example("test"))
    print(task.done())
    await task
    print(task.done())


async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')


async def s1():
    """4秒错误写法"""
    await a()
    await b()


async def c1():
    """3秒正确写法"""
    await asyncio.gather(a(), b())


async def c2():
    """3秒正确写法"""
    await asyncio.wait([a(), b()])


async def c3():
    """3秒正确写法"""
    task1 = asyncio.create_task(a())
    task2 = asyncio.create_task(b())
    await task1
    await task2


async def c4():
    """3秒正确写法"""
    task = asyncio.create_task(b())
    await a()
    await task


async def c5():
    """3秒正确写法"""
    task = asyncio.ensure_future(b())
    await a()
    await task


async def c6():
    """3秒正确写法"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(b())
    await a()
    await task


async def s2():
    """4秒错误写法"""
    task = asyncio.create_task(b())
    await task
    await a()


async def s3():
    """4秒错误写法"""
    # **直接await task不会对并发有帮助。asyncio.create_task是Python 3.7新增的高阶API，*是推荐的用法，其实你还可以用asyncio.ensure_future和loop.create_task：
    await asyncio.create_task(a())
    await asyncio.create_task(b())


def show_perf(func):
    print('*' * 20)
    start = time.perf_counter()
    asyncio.run(func())
    print(f'{func.__name__} Cost: {time.perf_counter() - start}')
