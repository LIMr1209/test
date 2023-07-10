import json
from multiprocessing import Process

import numpy as np
import time
import asyncio
import multiprocessing

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

num = 5

chunk_size = len(data1) // num

last_chunk_size = chunk_size + (len(data1) % num)

# 划分列表为多个子列表
chunks = [data1[i:i + chunk_size] for i in range(0, len(data1) - last_chunk_size, chunk_size)]

# 将多余的元素添加到最后一部分
chunks.append(data1[-last_chunk_size:])

uv_data = {}
# async def my_coroutine(o, start):
#     # 协程的具体逻辑
#     for j, i in enumerate(o):
#         array = np.tile(i, (data1.shape[0], 1))
#         equal = array == data2
#         test = np.logical_and.reduce(equal, axis=1)
#         indices = np.where(test)
#         t = np.ravel(indices).tolist()
#         if t:
#             uv_data[j + start] = t



manager = multiprocessing.Manager()
uv_data = manager.dict()

def my_coroutine(o, start, uv_data):
    # 协程的具体逻辑
    for j, i in enumerate(o):
        array = np.tile(i, (data1.shape[0], 1))
        equal = array == data2
        test = np.logical_and.reduce(equal, axis=1)
        indices = np.where(test)
        t = np.ravel(indices).tolist()
        if t:
            uv_data[j + start] = t

# 运行多个协程的函数
# async def run_coroutines():
#     # 创建一组协程任务
#     tasks = [my_coroutine(i, j * chunk_size) for j, i in enumerate(chunks)]
#     # 并行运行协程任务
#     await asyncio.gather(*tasks)


# 创建事件循环
# loop = asyncio.get_event_loop()
#
# # 在事件循环中运行协程
# loop.run_until_complete(run_coroutines())
#
# # 关闭事件循环
# loop.close()

processes = []
for j,i in enumerate(chunks):
    p = Process(target=my_coroutine, args=(i, j * chunk_size, uv_data))
    processes.append(p)
    p.start()

    # 等待所有进程完成
for p in processes:
    p.join()

uv_data = dict(uv_data)

with open("result1.json", "w") as f:
    json.dump(uv_data, f)

print("时间", time.time() - start)