# encoding:utf-8
import json
import os

import requests
import base64

'''
图像清晰度增强
'''
def baidu_enhance(path,new_path):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=P45TszBR1If7xRTV51uqEV3C&client_secret=IcbqmnQgyYGZFGZrwxEW9UmF39WQK6Ai'
    # response = requests.get(host)
    # if response:
    #     print(response.json())
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
    # 二进制方式打开图片文件
    f = open(path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.e640f683da9c5f38acebfe0930a293dc.2592000.1624772565.282335-22812256'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    res = json.loads(response.content)
    image = res['image']
    with open(new_path, 'wb') as f:
        f.write(base64.b64decode(image))


if __name__ == '__main__':
    path_name = 'C:/Users/aaa10/Desktop/chun_1024'
    newpath = 'C:/Users/aaa10/Desktop/chun_enhance'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item)).replace('\\', '/')
        baidu_enhance(full_path, newpath + '/' + dir_item)