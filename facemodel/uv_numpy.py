import json
import numpy as np
import time
#
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


start = time.time()
data2 = np.loadtxt("vertex_uv_coord_np.txt")

with open("10.json", "r") as f:
    temp = json.load(f)

data1 = np.array([[item['x'], item['y']] for item in temp])

uv_data = {}

for j, i in enumerate(data1):
    array = np.tile(i, (data1.shape[0],1))
    equal = array == data2
    test = np.logical_and.reduce(equal, axis=1)
    indices = np.where(test)
    t = np.ravel(indices).tolist()
    if t:
        uv_data[j] = t

with open("result.json", "w") as f:
    json.dump(uv_data, f)



# data2 = np.loadtxt("vertex_uv_coord_np.txt")
#
# with open("10.json", "r") as f:
#     temp = json.load(f)
#
# data1 = np.array([[item['x'], item['y']] for item in temp])
# #
#
# data1 = torch.from_numpy(data1).type(torch.double)
# data1.to(device="cuda:0")
# data2 = torch.from_numpy(data2).type(torch.double)
# data2.to(device="cuda:0")
#
#
# uv_data = {}
#
# for j, i in enumerate(data1):
#     array = torch.tile(i, (data1.shape[0],1))
#     equal = array == data2
#     test = torch.any(equal, dim=1, keepdim=True)
#     t = torch.nonzero(test.view(-1)).view(-1).tolist()
#     print(t)
#     if t:
#         uv_data[j] = t

# with open("result1.json", "w") as f:
#     json.dump(uv_data, f)
#
# print(len(uv_data))



# data1 = np.array([[1,2],[3,4]])
# data2 = np.array([[1,2],[3,4]])

# arr = np.expand_dims(data1,0).repeat(data2.shape[0],axis=1)
# arr2 = np.expand_dims(data2,0).repeat(data2.shape[0],axis=0)
# print(arr)
# arr2 = arr2.reshape(arr.shape)
# print(arr2)
# a = arr2 == arr
# test = np.logical_and.reduce(a, axis=1)
# print(test)
# indices = np.where(test)
# print(np.ravel(indices).tolist())
#
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
#
#


# import json
# import numpy as np
#
# # 加载第一个文件的数据
# with open("10.json", "r") as f:
#     data1 = json.load(f)
#
# # 加载第二个文件的数据，并转换为 NumPy 数组
# data2 = np.loadtxt("vertex_uv_coord_np.txt")
#
# # 使用 NumPy 的函数对数据进行筛选和映射
# indices = np.where(np.isin(data2, data1))
# uv_data = {i: indices[0][np.where(indices[1] == i)].tolist() for i in range(len(data1))}
# print(uv_data)
# print(len(uv_data))
print("运行时间：",time.time()-start)