# cython: language_level=3
cimport cython
from libc.string cimport memcmp
from libc.stdlib cimport malloc
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
    cdef point * ex = <point *> malloc(sizeof(point))
    return ex

cdef bint point_compare(dict[str, float] i, dict[str, float] j):
    cdef point* ex1 = create_point();
    ex1.x = i["x"]
    ex1.y = i["y"]
    cdef point * ex2 = create_point()
    ex2.x = j["x"]
    ex2.y = j["y"]
    if memcmp(ex1, ex2, sizeof(point)) == 0:
        return True
    else:
        return False




# 4秒
# 两个修饰符用来关闭 Cython 的边界检查
@cython.boundscheck(False)
@cython.wraparound(False)
cdef dict[str, int] _uv_compare(list[dict[str, float]] data1, list[dict[str, float]] data2):
    cdef dict[str, int] uv_data = {}
    cdef int count = 0
    for index1, i in enumerate(data1):
        for index2, j in enumerate(data2):
            if point_compare(i, j):
            # if i == j:
            # if i["x"] == j["x"] and i["y"] == j["y"]:
                if index1 in uv_data:
                    uv_data[str(index1)].append(index2)
                else:
                    uv_data[str(index1)] = [index2]
    # for i in range(20792):
    #     for j in range(20792):
    #         if i == j:
    #             count += 1
    return uv_data

# 在 Python 程序中，是看不到 cdef 的函数的，所以我们这里 def uv_compare(a, b) 来调用 cdef 过的 _uv_compare 函数。
def uv_compare(a, b):
    return _uv_compare(a, b)