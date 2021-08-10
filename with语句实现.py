class File(object):
    """
    使用__enter__和__exit__实现
    1、with语句先暂存了File类的__exit__方法，然后它调用File类的__enter__方法。
    2、__enter__方法打开文件并返回给with语句，打开的文件句柄被传递给opened_file参数。
    3、with语句调用之前暂存的__exit__方法，__exit__方法关闭了文件。
    """

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        """异常抛出，_exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出"""
        self.file_obj.close()
        print(type)
        print(value)
        print(traceback)
        return True


# with File('demo.txt', 'w') as opened_file:
#     opened_file.write('Hola!')
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')

import contextlib

"""
contextlib模块装饰器和生成器实现
yield之前的代码由__enter__方法执行，yield之后的代码由__exit__方法执行。本质上还是__enter__和__exit__方法。
"""


@contextlib.contextmanager
def my_open(file_name, method):
    file = open(file_name, method)
    try:
        yield file
    except Exception as e:
        print(str(e))
    finally:
        file.close()


with my_open('demo.txt', 'w') as f:
    f.write('12312111111')

with my_open('demo.txt', 'a') as f1,my_open('demo.txt','a') as f2:
    f1.write('yyyyyy')
    f2.write('12312111112')
