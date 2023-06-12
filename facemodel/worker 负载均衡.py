import multiprocessing
import time

import requests

def test():
    start = time.time()
    files = {'file': ('20230509-173935.png', open('20230509-173935.png', 'rb'), 'image/png')}
    headers={"cookie":"session=f95244f8-efd6-4a71-8b3c-839d63316ec4.JwjapiX7UXPG83JM59Ky2cGMZr4"}
    response = requests.post("http://10.25.20.15:8011/api2/api/creation/create_image",files=files,headers=headers)
    print(response.content.decode("utf-8"))
    end = time.time()
    print("时间", end-start)


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    num = 30
    for i in range(num):
        pool.apply_async(test)
    pool.close()
    pool.join()