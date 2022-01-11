from __future__ import annotations


# 内置的 “断点” breakpoint()
def guess(target):
    user_guess = "100"
    # breakpoint() # 设置断点
    # 以前
    # import pdb; pdb.set_trace()
    if user_guess == target:
        return "你猜对了!"
    else:
        return "猜错了"


# dataclasses 数据类
# 新的 dataclass() 装饰器提供了一种声明 数据类 的方式。 数据类使用变量标注来描述其属性。 它的构造器和其他魔术方法例如 __repr__(), __eq__() 以及 __hash__() 会自动地生成。

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # 有默认值

    # 额外初始化
    def __post_init__(self):
        self.v = 1


p = Point(1.5, 2.5)
q = Point(1.5, 2.5, 1)
print(p)  # produces "Point(x=1.5, y=2.5, z=0.0)"
print(q)


# 类型提示的强化
# Python 的类型系统具有很强的表现力，但是导致非常痛苦的一个问题是前向引用。类型提示，或者更通用的注解，它们是在模块被导入时进行计算。因此所有的名称必须已经在他们使用之前被定义。下面这段代码就是不对的：
# 运行这段代码将会引发 NameError，因为类 Tree 在 .__init__() 方法定义的时候还没完成定义：

# 为了避免这个，你需要将 "Tree" 作为一个字符串：
# class Tree:
#     def __init__(self, left: "Tree", right: "Tree") -> None:
#         self.left = left
#         self.right = right


# python 3.7 中，前向引用已经可以通过 __future__ import 使用。现在你可以这样写了：
# from __future__ import annotations # 必须出现在文件的第一行


class Tree:
    def __init__(self, left: Tree, right: Tree) -> None:
        self.left = left
        self.right = right


#

# 生成器异常处理
'''
在Python 3.7中，生成器引发StopIteration异常后，StopIteration异常将被转换成RuntimeError异常，那样它不会悄悄一路影响应用程序的堆栈框架。这意味着如何处理生成器的行为方面不太敏锐的一些程序会在Python 3.7中抛出RuntimeError。在Python 3.6中，这种行为生成一个弃用警告；在Python 3.7中，它将生成一个完整的错误。

一个简易的方法是使用try/except代码段，在StopIteration传播到生成器的外面捕获它。更好的解决方案是重新考虑如何构建生成器――比如说，使用return语句来终止生成器，而不是手动引发StopIteration。
'''

# 开发模式
"""
Python解释器添加了一个新的命令行开关：-X，让开发人员可以为解释器设置许多低级选项。

这种运行时的检查机制通常对性能有重大影响，但在调试过程中对开发人员很有用。

-X 激活的选项包括：

asyncio模块的调试模式。这为异步操作提供了更详细的日志记录和异常处理，而异常操作可能很难调试或推理。
面向内存分配器的调试钩子。这对于编写CPython扩展件的那些人很有用。它能够实现更明确的运行时检查，了解CPython如何在内部分配内存和释放内存。
启用faulthandler模块，那样发生崩溃后，traceback始终转储出去。
"""

# 高精度时间函数
# 新的时间函数使用后缀_ns。比如说，time.process_time()的纳秒版本是time.process_time_ns()。请注意，并非所有的时间函数都有对应的纳秒版本。
import time

print(time.process_time())
print(time.process_time_ns())

# "asyncio" 重大改进
# asyncio 模块被从 Python 3.4 中引入去用事件循环，协程和 futures 的现代化方式处理并发。这里有个详细介绍。
#
# Python 3.7 中，asyncio 模块取得了重大进展，包括许多新的函数，支持上下文变量（看这里）以及性能改进。特别值得注意的是 asyncio.run()，它简化了同步代码调用协程。使用 asyncio.run() 你不必再去显示地创建事件循环。一个异步的 Hello World 程序可以这样写了：

# "async"和"await" 是关键字
# Python 3.5 中介绍了 基于 async 和 await 语法的协程。为了避免向后兼容问题，async  和 await 并未添加到保留关键字列表。换句话说，仍然可以定义名为 async 和 await 的变量或者函数。
#
import asyncio


async def hello_world():
    print("Hello World!")


asyncio.run(hello_world())
# asyncio.get_event_loop().run_until_complete(hello_world())


# 新增contextvars模块，针对异步任务提供上下文变量
"""
上下文变量是根据其上下文可以具有不同值的变量。它们类似于本地线程存储，一个变量在每个执行线程可能具有不同的变量值。但是，对于上下文变量，在一个执行线程中可能存在多个上下文。上下文变量的主要用例是跟踪并发异步任务中的变量。

下面的示例构造了三个上下文，每个上下文都有自己的 name 值。 greet() 函数在之后的每一个上下文中都可以使用 name 的值：
"""
import contextvars

name = contextvars.ContextVar("name")
contexts = list()


def greet():
    print(f"Hello {name.get()}")


# 构造上下文并设置上下文变量名称
for first_name in ["Steve", "Dina", "Harry"]:
    ctx = contextvars.copy_context()
    ctx.run(name.set, first_name)
    contexts.append(ctx)

# 在每个上下文中运行 greet 函数
for ctx in reversed(contexts):
    ctx.run(greet)

# python3.6 安装 httpx 依赖 contextvars, 和celery 冲突

# 字典现在保持插入顺序。这在 3.6 中是非正式的，但现在成为了官方语言规范。在大多数情况下，普通的 dict 能够替换 collections.OrderedDict。
a = {'1': 1}
a['2'] = 2
a[3] = '3'
print(a)
