import json

import numpy
import numpy as np
import time

start = time.time()

data2 = np.loadtxt("vertex_uv_coord_np(1).txt")

with open("10.json", "r") as f:
    temp = json.load(f)

data1 = np.array([[item['x'], item['y']] for item in temp])
# #
# if data1.shape != data2.shape:
#
#     if data1.shape[0] < data2.shape[0]:
#         new_arr = np.zeros(data2.shape)
#         new_arr[:data1.shape[0], :] = data1
#         data1 = new_arr
#     else:
#         new_arr = np.zeros(data1.shape)
#         new_arr[:data2.shape[0], :] = data2
#         data2 = new_arr
#
# uv_data = {}
#
# for j, i in enumerate(data1):
#     array = np.tile(i, (data1.shape[0],1))
#     equal = array == data2
#     test = np.logical_and.reduce(equal, axis=1)
#     indices = np.where(test)
#     uv_data[j] = np.ravel(indices).tolist()

# print(uv_data)
# print(len(uv_data))



# data1 = np.array([[1,2],[3,4]])
# data2 = np.array([[1,2],[3,4]])

arr = np.expand_dims(data1,0).repeat(data2.shape[0],axis=1)
arr2 = np.expand_dims(data2,0).repeat(data2.shape[0],axis=0)
print(arr)
arr2 = arr2.reshape(arr.shape)
print(arr2)
a = arr2 == arr
test = np.logical_and.reduce(a, axis=1)
print(test)
indices = np.where(test)
print(np.ravel(indices).tolist())

# with open("10.json", "r") as f:
#     data1 = json.load(f)
#
# data2 = []
# with open("vertex_uv_coord_np(1).txt", "r") as f:
#     for i in f:
#         xy = i.split()
#         data2.append({"x": float(xy[0]), "y": float(xy[1])})
# uv_data = {}
# #
# for index1, i in enumerate(data1):
#     # delete_data2_index = []
#     for index2, j in enumerate(data2):
#         if i == j:
#             if index1 in uv_data:
#                 uv_data[index1].append(index2)
#             else:
#                 uv_data[index1] = [index2]
#
#             # delete_data2_index.append(index2)
#     # for index2 in delete_data2_index:
#     #     data2.pop(index2)
#
# print(json.dumps(uv_data))
# print(len(uv_data))


print("运行时间：",time.time()-start)