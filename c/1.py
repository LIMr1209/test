from ctypes import Structure, c_char, c_int, CDLL, c_double
from ctypes import POINTER, cast

import json

with open("10.json", "r") as f:
    data1 = json.load(f)

data2 = []
with open("vertex_uv_coord_np.txt", "r") as f:
    for i in f:
        xy = i.split()
        data2.append({"x": float(xy[0]), "y": float(xy[1])})


# 定义Person结构体
class Point(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double)]


class UvData(Structure):
    _fields_ = [("key", c_int),
                ("value", c_int)]


# 加载共享库
lib = CDLL('./hash_table.so')

# 声明C函数原型
lib.uv_compare.restype = POINTER(UvData)
lib.uv_compare.argtypes = (POINTER(Point), POINTER(Point))

data_1 = (Point * len(data1))()

for j, i in enumerate(data1):
    data_1[j].x = i["x"]
    data_1[j].y = i["y"]

data_2 = (Point * len(data2))()
for j, i in enumerate(data2):
    data_2[j].x = i["x"]
    data_2[j].y = i["y"]

uv_data = {}

# 调用C函数并传递结构体参数
v = lib.uv_compare(data_1, data_2)
result_array = cast(v, POINTER(UvData * 20792)).contents
for i in range(20792):
    struct = result_array[i]
    a = struct.key
    b = struct.value
    if a not in uv_data:
        uv_data[a] = [b]
    else:
        uv_data[a].append(b)

print(json.dumps(uv_data))
