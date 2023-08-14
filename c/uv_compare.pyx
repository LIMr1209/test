# cython: language_level=3
cimport cython
from libc.string cimport memcmp
from libc.stdlib cimport malloc
from typing import List, Dict

# cimport 是 Cython 中用来引入 .pxd 文件的命令
# Cython 程序的扩展名是 .pyx

# 6秒
# def uv_compare(data1, data2):
#     uv_data = {}
#     count = 0
#     for index1, i in enumerate(data1):
#         for index2, j in enumerate(data2):
#             if i == j:
#                 if index1 in uv_data:
#                     uv_data[index1].append(index2)
#                 else:
#                     uv_data[index1] = [index2]
#     return uv_data


cdef struct point:
    double x
    double y

cdef point* create_point():
    cdef point * ex = <point *> malloc(20792 * sizeof(point))
    return ex


# 0.2 秒
# 两个修饰符用来关闭 Cython 的边界检查
@cython.boundscheck(False)
@cython.wraparound(False)
cdef dict[str, int] _uv_compare(List[Dict[str, float]] data1, List[Dict[str, float]] data2):
    data_1 = create_point()
    data_2 = create_point()
    for j, i in enumerate(data1):
        data_1[j].x = i["x"]
        data_1[j].y = i["y"]

    for j, i in enumerate(data2):
        data_2[j].x = i["x"]
        data_2[j].y = i["y"]

    cdef Dict[str, int] uv_data = {}

    for index1 in range(20792):
        for index2 in range(20792):
            if memcmp(&data_1[index1], &data_2[index2], sizeof(point))==0:
                if index1 in uv_data:
                    uv_data[str(index1)].append(index2)
                else:
                    uv_data[str(index1)] = [index2]

    return uv_data

# 在 Python 程序中，是看不到 cdef 的函数的，所以我们这里 def uv_compare(a, b) 来调用 cdef 过的 _uv_compare 函数。
def uv_compare(a, b):
    return _uv_compare(a, b)