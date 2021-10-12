import time
import asyncio
import requests
from bson import ObjectId


# 随机生成BsonId
def gen_mongo_id():
    return ObjectId().__str__()


# 上传图片到七牛-core
async def upload_core(id):
    try:
        print("开始上传 id ", id)
        int('aa')
    except Exception as e:
        print(str(e))


def upload():
    page = 1
    is_end = False
    loop = asyncio.get_event_loop()
    while not is_end:
        print("current page %s: \n" % page)
        start = time.time()
        data = list(range((page - 1) * 100, page * 100))
        task = []
        for i, image in enumerate(data):
            task.append(upload_core(i))
        loop.run_until_complete(asyncio.wait(task))
        asyncio.run(asyncio.wait(task))
        page += 1
        print(time.time() - start)
        if page == 10:
            is_end = True
    loop.close()
    print("is over execute count")


if __name__ == '__main__':
    import urllib3

    requests.packages.urllib3.disable_warnings()
    urllib3.disable_warnings()
    upload()
