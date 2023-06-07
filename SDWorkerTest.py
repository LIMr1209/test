import json
import multiprocessing
import requests
import time


def send_request():
    print("start")
    start = time.time()
    response = requests.post("http://10.25.20.15:8000/api/creation/create_image", headers={"cookie":"session=0e9071e0-5dbf-4034-9521-379f23290790.aS1Xp-otLaQAPYksAiiJgki-qtM"},
                             files={"file": ("1.png", open("/home/limr/Desktop/图片/20230509-173935.png", 'rb'), "image/png")})
    if response.status_code != 200:
        print("错误")
        return
    res = json.loads(response.content.decode("utf-8"))
    print(res)
    end = time.time()
    print(end - start)
    print("结束 时间", end - start)


if __name__ == '__main__':
    num = 24
    pool = multiprocessing.Pool(num)
    for i in range(num):
        pool.apply_async(send_request)
    try:
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        pass
