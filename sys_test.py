#!/usr/bin/env python
# coding=utf-8
import inspect
import sys

try:
    import requests
except:
    pass


def get_previous_frame():
    """获取上一级调用堆栈帧"""
    previous_frame = inspect.currentframe().f_back  # 获取上一个堆栈帧
    calling_function_name = previous_frame.f_code.co_name  # 获取调用本函数的函数名
    calling_line_number = previous_frame.f_lineno  # 获取调用本函数的行号
    calling_file_name = previous_frame.f_globals['__file__']  # 获取调用本函数的文件名

    print("Calling function:", calling_function_name)
    print("Line number:", calling_line_number)
    print("File name:", calling_file_name)


# 在 Python 中，sys.stdout.flush() 是用于强制将缓冲区中的数据刷新到标准输出流（stdout）的方法。
# 标准输出通常是行缓冲的，这意味着输出的内容会存储在缓冲区中，直到缓冲区满了或者遇到换行符 \n 才会被刷新到终端。但有时，你可能希望立即将缓冲区的内容输出，而不需要等待缓冲区填满或遇到换行符。这时就可以使用 sys.stdout.flush() 方法。
# 通常情况下，不需要手动调用 sys.stdout.flush()，因为当程序结束时，缓冲区会自动被刷新。但在某些特定的场景中，比如实时日志记录或与其他进程进行交互时，可能需要手动刷新缓冲区来确保及时输出。

def sys_demo():
    get_previous_frame()
    # 默认编码
    print(sys.getdefaultencoding())

    # Python版本
    print(sys.version)

    # 添加模块路径到搜索路径
    sys.path.append("./module")

    # (函数)打印异常信息
    try:
        1 / 0
    except:
        types, value, back = sys.exc_info()  # 捕获异常
        # sys.excepthook(types, value, back)  # 打印异常

    # 输入和输出
    sys.stdout.write(">> ")
    sys.stdout.flush()
    strs = sys.stdin.readline()[:-1]
    sys.stderr.write("输入的内容为: {}".format(strs))
    sys.stderr.flush()


def sys_func():
    lists = sys.argv  # 传递给Python脚本的命令行参数列表 => python p.py -> ['p.py'] / python p.py a 1 -> ['p.py', 'a', '1'] / 程序内执行 -> ['']
    strs = sys.getdefaultencoding()  # 默认字符集名称
    strs = sys.getfilesystemencoding()  # 系统文件名字符集名称
    a = "你好啊"
    b = a
    num = sys.getrefcount(a)  # 返回object的引用计数(比实际多1个)
    num1 = sys.getrefcount(b)
    dicts = sys.modules  # 已加载的模块, 可修改, 但不能通过修改返回的字典进行修改
    lists = sys.path  # 模块搜索路径
    sys.path.append("./test")  # 动态添加模块搜索路径
    strs = sys.platform  # 平台标识符(系统身份进行详细的检查,推荐使用) Linux:'linux' / Windows:'win32' / Cygwin:'cygwin' / Mac OS X:'darwin'
    version = sys.version  # python解释器版本
    # lists = sys.thread_info  # 线程信息
    api_version = sys.api_version  # 解释器C API版本

    types, value, back = sys.exc_info()  # 捕获异常 详见 异常 文章的 excep() 代码块第二小部分(http://blog.csdn.net/rozol/article/details/69313164)
    # sys.excepthook(types, value, back)  # 打印异常
    # types = sys.last_type
    # value = sys.last_value
    # back = sys.last_traceback
    # 它们是在不处理异常和解释器打印错误消息和堆栈回溯时设置的。它们的预期用途是允许交互式用户导入调试程序模块并进行事后调试，而不必重新执行导致错误的命令。
    # sys.exit([arg]) // 引发SystemExit异常退出Python(可以try), 范围[0,127], None==0, "string"==1
    # sys.exit(0)

    limit = sys.getrecursionlimit()  # 最大递归数(堆栈最大深度), 详见 函数 文章(http://blog.csdn.net/rozol/article/details/69242050)
    sys.setrecursionlimit(5000)  # 修改最大递归数
    limit = sys.getrecursionlimit()
    fnum = sys.getswitchinterval()  # 获取线程切换间隔
    sys.setswitchinterval(0.005)  # 设置线程切换间隔, 单位秒
    # num = sys.getcheckinterval()  # 解释器的检查间隔  遗弃
    # sys.setcheckinterval(100)  # 设置解释器检查间隔, 执行(默认)100个虚拟指令执行一次检查, 值为<=0时,检查每个虚拟指令 遗弃

    # sys.stdin // 标准输入流
    # strs = sys.stdin.readline()[:-1]
    # # sys.stdout // 标准出入输出
    # sys.stdout.write(">>")
    # sys.stdout.flush()
    # # sys.stderr // 标注错误流
    # sys.stderr.write(">>")

    # ---

    lists = sys.builtin_module_names  # 所有模块 (注:非导入模块)
    path = sys.base_exec_prefix  # Python安装路径
    path = sys.base_prefix  # 同base_exec_prefix
    path = sys.exec_prefix  # 同base_exec_prefix
    path = sys.prefix  # 同base_exec_prefix
    path = sys.executable  # Python解释器的绝对路径

    strs = sys.byteorder  # 本机字节顺序指示器, big-endian(最高有效字节在第一位)值为'big', little-endian(最低有效字节在第一位)值为'little'
    strs = sys.copyright  # python版权
    num = sys.hexversion  # 16进制版本号
    lists = sys.implementation  # 当前运行的解释器的信息
    num = sys.getallocatedblocks()  # 解释器当前分配的内存块的数量
    boolean = sys.dont_write_bytecode  # 是否不会尝试导入源模块是写入.pyc文件 (False会写入.pyc文件)
    # sys.getsizeof(object[, default]) // 返回对象的大小bit, 只计算自身内存消耗,不计算引用对象的内存消耗, 调用对象的__sizeof__(), default没有获取到默认返回值
    num = sys.getsizeof(1002032132)
    boolean = sys.is_finalizing()  # 解释器是否正在被关机
    num = sys.maxsize  # 最大整数值(2 ** 31 -1), 与系统有关
    num = sys.maxunicode  # 最大Unicode值的整数 (1114111)
    # strs = sys.ps1  # 解释器主提示符
    # strs = sys.ps2  # 解释器次提示符

    # sys.call_tracing(test, ("arg",2))  # 调用函数
    # sys._clear_type_cache()  # 清除内部类型缓存
    # sys._debugmallocstats()  # 打印CPython内存分配器状态的低级信息

    # sys.setprofile(profilefunc)  # 设置profile函数, 默认None
    a = sys.getprofile()  # 获取profile函数
    # sys.settrace(tracefunc)  # 设置跟踪函数, def tracefunc(frame、event 和arg):
    b = sys.gettrace()  # 获取跟踪函数, 默认None
    # sys.set_coroutine_wrapper(wrapper)  # 设置包装 def wrapper(coro):
    c = sys.get_coroutine_wrapper()  # 包装, 默认None

def test(a, b):
    print(a)
    print(b)


if __name__ == "__main__":
    # sys_demo()
    sys_func()


    # import sys
    #
    # def my_profiler(frame, event, arg):
    #     # 在这里编写你的跟踪逻辑
    #     print(f"Tracing: {event} at line {frame.f_lineno} of {frame.f_code.co_filename}")
    #     print(arg)
    #     return my_profiler
    #
    # # 设置跟踪器
    # sys.setprofile(my_profiler)
    #
    # # 调用一个函数
    # def my_function():
    #     print("Inside my_function")
    #
    # my_function()


    # import sys
    #
    # def my_tracer(frame, event, arg):
    #     # 在这里编写你的追踪逻辑
    #     print(f"Tracing: {event} at line {frame.f_lineno} of {frame.f_code.co_filename}")
    #     print(arg)
    #     return my_tracer
    #
    # # 设置追踪器
    # sys.settrace(my_tracer)
    #
    # def aaa():
    #     print("aaa")
    #
    # # 调用一个函数
    # def my_function():
    #     print("Inside my_function")
    #     # return aaa()
    #
    # my_function()
    #
    # # 停止追踪器
    # sys.settrace(None)
