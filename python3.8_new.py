# 海象运算符
# 新增的语法 := 可在表达式内部为变量赋值
import re
from functools import lru_cache

if result := re.search(r'\d{11}', 'my mobile number is 17635700440'):  # 正则使用
    print(result.group())

f = open('python3.8_new.py', 'rb')  # 文件读取使用
n = 1
while line := f.readline():
    n += 1
print(n)

stuff = [(y := x + 1, x / y) for x in range(5)]  # 列表推导式使用
print(stuff)


# Positional-only parameters 以/来表示，用来分割位置参数和关键字参数，/前的所有参数只能通过位置来进行传参，/后面的参数可位置传参课关键字传参。

def f(a, b, /, c, d, e, f):
    print(a, b, c, d, e, f)


f(1, 2, c=3, d=4, e=5, f=6)
#  f(a=1, b=2, c=3, d=4, e=5, f=6) # f() got some positional-only arguments passed as keyword arguments: 'a, b'

# 加强 f-string

balance = 1000
print(f'Account balance = {balance}')  # python3.6
print(f'Account {balance = }')  # python3.8

# Python Runtime Audit Hooks审计钩子
import sys
import urllib.request


def audit_hook(event, args):
    """他将调用栈以及参数全部打印出来了，这就有点像服务器开发里面的middleware。"""
    print(event, args)


# sys.addaudithook(audit_hook)

# urllib.request.urlopen('http://www.baidu.com')

# 新模块importlib.metadata
# importlib.metadata支持读取第三方库的元数据，比如库的版本号，依赖库等等。这个特性有点鸡肋的，因为其实可以直接用魔法属性__version__访问到，具体用法如下；

from importlib.metadata import version, requires, files

# print(version('requests')) # 版本号
# print(requires('requests')) # 依赖库
# print(requires('requests')) # 路径
#

# 反向迭代字典
a = {'a': 1, 'b': 2}
for i in a.items().__reversed__():  # 反向迭代字典
    print(i)


# lru_cache
import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

start_1 = time.perf_counter()
fib(30)
# 如果要求斐波拉契数列的第50项，调用fib(50)可能就要等到地老天荒了，因为有大量已经计算过的值被重新算了一遍，而这个重新算的次数随着n的增长是指数级别的，耗费了大量时间。所以我们一般会先用一个dict来cache一下数据，像这样

dic = {0: 1, 1: 1}
def fib_dict(n):
    if item:=dic.get(n):
        return item
    dic[n-2],dic[n-1] = fib(n-2), fib(n-1)
    return dic[n-2]+dic[n-1]
fib_dict(30)

# 使用 lru_cache
@lru_cache
def fib_cache(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-2)+fib(n-1)

fib_cache(30)
