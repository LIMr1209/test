import os
import inspect


# 调用者的帧比当前帧高一帧。您可以使用inspect.currentframe().f_back来查找调用者的框架。然后使用inspect.getframeinfo获取调用者的文件名和行号。


def get_cur_info():
    try:
        current_frame = inspect.currentframe().f_back
        return os.path.basename(current_frame.f_code.co_filename), current_frame.f_lineno, current_frame.f_code.co_name
    except ValueError:
        return 'unknown', 0, 'unknown'


def produce():
    return get_cur_info()


def business():
    return produce()


if __name__ == '__main__':
    # print(get_cur_info())  # 输出 ('unknown', 0, 'unknown')
    #
    # print(produce())  # 输出 ('a.py', 22, '<module>')
    #
    # print(business())  # 输出 ('a.py', 16, 'business')

    for i in range(1):
        print(i)

