import json
import time
from urllib.parse import urlparse
import asyncio
import requests
import httpx
from qiniu import Auth, put_data, put_file
from bson import ObjectId

# 随机生成BsonId
def gen_mongo_id():
    return ObjectId().__str__()


# 上传图片到七牛-core
async def upload_core(image, ignore_gif=True, ignore_size=True, ignore_timeout=True):
    print("开始上传,图片ID: %s" % str(image["_id"]))
    result = {"success": False, "message": ""}
    if image["url"] == "local_image":
        result["message"] = "本地图片 %s" % str(image["_id"])
        return result
    file_path = urlparse(image["url"]).path
    if not ignore_gif:
        if file_path.endswith(".gif"):
            result["message"] = "gif图片 %s" % str(image["_id"])
            return result
    if not image["path"]:
        bucket_name = "frbird"
        accessKey = 'ERh7qjVSy0v42bQ0fftrFeKYZG39XbzRlaJO4NFy'
        secretKey = 'r-NUrKsnRBEwTQxbLONVrK9tPuncXyHmcq4BkSc7'
        key = "%s/%s/%s" % (
            "image",
            time.strftime("%y%m%d"),
            gen_mongo_id(),
        )
        try:
            # 构建鉴权对象
            q = Auth(accessKey, secretKey)
            # 生成上传 Token，可以指定过期时间等
            policy = {
                "callbackUrl": 'https://www.taihuoniao.com/api/image/rollback?id=%s'%str(image["_id"]),
                "callbackBody": "name=$(fname)&filesize=$(fsize)&w=$(imageInfo.width)&h=$(imageInfo.height)",
            }
            token = q.upload_token(bucket_name, key, 3600, policy)
            if image["img_url"]:
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                }
                if not ignore_timeout:
                    # head = requests.head(
                    #     image["img_url"], timeout=(3, 30), verify=False
                    # )
                    async with httpx.AsyncClient() as client:
                        head = await client.head(image["img_url"], timeout=(3, 30))
                else:
                    # head = requests.head(image["img_url"], verify=False)
                    async with httpx.AsyncClient() as client:
                        head = await client.head(image["img_url"])
                if not ignore_size:
                    if "Content-Length" in head.headers:
                        size = head.headers["Content-Length"]
                        if int(size) >= 1024 * 1024 * 5:
                            result["message"] = "图片大于5m %s" % str(image._id)
                            return result
                if not ignore_gif:
                    if "Content-Type" in head.headers:
                        image_type = head.headers["Content-Type"]
                        if image_type == "image/gif":
                            result["message"] = "gif图片 %s" % str(image["_id"])
                            return result
                if not ignore_timeout:
                    # response = requests.get(
                    #     image["img_url"], headers=headers, timeout=(3, 30), verify=False
                    # )
                    async with httpx.AsyncClient() as client:
                        response = await client.get(image["img_url"],timeout=(3, 30))
                else:
                    # response = requests.get(
                    #     image["img_url"], headers=headers, verify=False
                    # )
                    async with httpx.AsyncClient() as client:
                        response = await client.get(image["img_url"])
                if response.status_code == 200:
                    ret, info = put_data(token, key, response.content)
                else:
                    result["message"] = "获取图片错误 %s %s" % (
                        response.status_code,
                        str(image["_id"]),
                    )
                    if response.status_code == 403:
                        with open("403.txt", "a") as f:
                            f.write(str(image["_id"]) + "\t")
                    if response.status_code == 404:
                        with open("404.txt", "a") as f:
                            f.write(str(image["_id"]) + "\t")
                    return result
            else:
                result["message"] = "图片地址不存在ID %s" % str(image["_id"])
                return result
            if not info.status_code == 200:
                result["message"] = "上传七牛失败 %s" % info.error
                return result
            try:
                async with httpx.AsyncClient() as client:
                    res = await client.post("https://www.taihuoniao.com/api/image/upload_submit",data={"path": key, "id": str(image["_id"])})
                # res = requests.post("https://www.taihuoniao.com/api/image/upload_submit",data={"path": key, "id": str(image["_id"])})
            except:
                await asyncio.sleep(3)
                async with httpx.AsyncClient() as client:
                    res = await client.post("https://www.taihuoniao.com/api/image/upload_submit",data={"path": key, "id": str(image["_id"])})
                # res = requests.post("https://www.taihuoniao.com/api/image/upload_submit",
                #                     data={"path": key, "id": str(image["_id"])})
            res = json.loads(res.content)
            if res["code"] == 0:
                result["success"] = True
                result["message"] = "上传七牛云成功 %s" % str(image["_id"])
            else:
                result["message"] = "上传七牛云失败 %s" % str(image["_id"])
        except Exception as e:
            result["message"] = "上传七牛云失败 %s  %s" % (str(e), str(image["_id"]))
    else:
        result["success"] = True
        result["message"] = "图片已处理 %s" % str(image["_id"])
    print(result)
    return result



def upload(ignore_gif=True, ignore_size=True, ignore_timeout=True):
    page = 1
    is_end = False
    loop = asyncio.get_event_loop()
    while not is_end:
        print("current page %s: \n" % page)
        start = time.time()
        response = requests.get(
            "https://www.taihuoniao.com/api/image/upload_list?page=%s&per_page=50" % page
        )
        res = json.loads(response.content)
        data = res["data"]
        task = []
        for i, image in enumerate(data):
            task.append(upload_core(image, ignore_gif, ignore_size, ignore_timeout))
        loop.run_until_complete(asyncio.wait(task))
        asyncio.run(asyncio.wait(task))
        page += 1
        print(time.time() - start)
        if page == res["total_page"]:
            is_end = True
    loop.close()
    print("is over execute count")


if __name__ == '__main__':
    import urllib3
    requests.packages.urllib3.disable_warnings()
    urllib3.disable_warnings()
    upload()
