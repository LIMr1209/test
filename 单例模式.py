# 装饰器（decorator）可以动态地修改一个类或函数的功能
import functools
import threading


def singleton(cls):
    """装饰器模式"""
    __instance = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return get_instance


@singleton
class MyClass(object):
    a = 1


# b = MyClass()
# c = MyClass()
# print(b is c)


class SingletonNew(object):
    """__new__方法实现"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SingletonNew, cls).__new__(cls, *args, **kwargs)
            # 可以在这里给实力对象绑定一些固有属性
            # cls.__instance.appkey = ""
        return cls.__instance


# b = SingletonNew()
# c = SingletonNew()
# print(b is c)


class SingletonMeta(type):
    "元类方式"
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


# python2写法
# class MyClass(object):
#     __metaclass__ = SingletonMeta()

# python3写法
class MyMetaClass(metaclass=SingletonMeta):
    def __init__(self):
        self.blog = "blog"


# b = MyMetaClass()
# c = MyMetaClass()
# print(b is c)


# 线程安全单例模式

def make_synchronized(func):
    func.__lock__ = threading.Lock()

    # 用装饰器实现同步锁
    def synced_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return synced_func

class Singleton(object):
    __instance = None

    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.blog = "blog"


def worker():
    e = Singleton()
    print(id(e))


if __name__ == "__main__":
    tasks = [threading.Thread(target=worker) for _ in range(20)]
    for task in tasks:
        task.start()
        task.join()
