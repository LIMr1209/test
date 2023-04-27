# import json
# import time
#
# start = time.time()
# #
# # with open("1.json", "r") as f:
# #     data1 = json.load(f)
# #
# # with open("2.json", "r") as f:
# #     data2 = json.load(f)
#
#
# data2 = []
# with open("202303311830316426b647bebb09c63681a00b_uvcoords.txt", "r") as f:
#     for i in f:
#         xy = i.split()
#         data2.append({"x": float(xy[0]), "y": float(xy[1])})
#
# with open("StandardUvData1.json", "r") as f:
#     data1 = json.load(f)
#
# data = {}
#
# # new_data2 = []
# # for i in data2:
# #     if i not in new_data2:
# #         new_data2.append(i)
#
#
# for index1, i in enumerate(data1):
#     delete_data2_index = []
#     for index2, j in enumerate(data2):
#         if i["x"] == j["x"] and i["y"] == j["y"]:
#             # print("坐标: " + str(index1) + " " + str(index2))
#             # print("i:", i)
#             # print("j:", j)
#             if index1 in data:
#                 data[index1].append(index2)
#             else:
#                 data[index1] = [index2]
#
#             delete_data2_index.append(index2)
#     for index2 in delete_data2_index:
#         data2.pop(index2)
#
# end = time.time()
#
# print(data)
# #
# # #
# # num = 0
# # for key, value in data.items():
# #     if len(value)>1:
# #         num += 1
# #         # print(key)
# # #
# # print(num)
# #
# # with open("res.json", "w") as f:
# #     json.dump(data, f)
#
# # print(end - start)
#
#
# # for index1, i in enumerate(data1):
# #     for index2, j in enumerate(data1):
# #         if index1 != index2:
# #             if i == j:
# #                 num += 1
# #
# #
# # print(num)