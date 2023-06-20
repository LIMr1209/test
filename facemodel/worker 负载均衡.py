import multiprocessing
import time

import aiohttp as aiohttp
import requests


def test():
    start = time.time()
    files = {'file': ('20230509-173935.png', open('20230509-173935.png', 'rb'), 'image/png')}
    headers = {"cookie": "session=77c73335-2fe5-426f-baaa-4e5f1b4c4383.qzHODjt56lZZLYLS_XDq3KTHYeQ"}
    response = requests.post("http://10.25.20.11:8000/api/creation/create_image", files=files, headers=headers)
    print(response.content.decode("utf-8"))
    end = time.time()
    print("时间", end - start)


# async def test2():
#     for i in range(3):
#         start = time.time()
#         files = {'file': ('20230509-173935.png', open('20230509-173935.png', 'rb'), 'image/png')}
#         headers = {"cookie": "session=f95244f8-efd6-4a71-8b3c-839d63316ec4.JwjapiX7UXPG83JM59Ky2cGMZr4"}
#         async with aiohttp.ClientSession() as session:
#             async with session.post("http://10.25.20.11:8000/api/creation/create_image", files=files,
#                                     headers=headers) as response:
#                 print(response.content.decode("utf-8"))
#         end = time.time()
#         print("时间", end - start)


if __name__ == '__main__':
    num = 5
    for i in range(num):
        pool = multiprocessing.Pool()
        for i in range(3):
            pool.apply_async(test)
            # pool.apply(test2)
        pool.close()
        pool.join()