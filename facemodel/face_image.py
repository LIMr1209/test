import json
import requests
import pathlib
import pdb
import re

path = "/home/limr/Downloads/测试首页图片11正式服v1.0.3"

base_url = "http://10.25.20.15:8000"

def post_image(filepath, name, cue_word):
    response = requests.post(url="{}/admin/face_image_auto/save".format(base_url), files={'file': open(filepath, 'rb')},
                             data={"name": name, "cue_word": cue_word}, headers={"cookie":"session=0e9071e0-5dbf-4034-9521-379f23290790.aS1Xp-otLaQAPYksAiiJgki-qtM"})
    if response.status_code != 200:
        return 0
    else:
        res = json.loads(response.content)
        print(res)
        if res["err"]:
            return 0
    return 1


def func(dir_path):
    for i in dir_path.iterdir():
        if i.is_dir():
            func(i)
        else:
            try:
                dir_name = str(dir_path).rsplit("/", 1)[1]
                name = dir_name.split("，", 1)[0]
                try:
                    # cue_word = dir_name.split("，", 1)[1]
                    cue_word = dir_name
                except:
                    cue_word = ""
                print("name", name)
                print("cue_word", cue_word)
                print("*****")
                res = post_image(str(i), name, cue_word)
                if not res:
                    print(str(i), name, cue_word)
            except Exception as e:
                print(str(e))
                print(dir_path)

def new_post_image(filepath, name):
    response = requests.post(url="{}/admin/face_image_auto/save_sd".format(base_url), files={'file': open(filepath, 'rb')},
                             data={"name": name}, headers={"cookie":"session=e1f70a5b-57b7-44ac-8194-37e1e5c91c7e.q1VsTc1ElUFvbh3D0V7qPHeCIY4"})
    print(response)
    if response.status_code != 200:
        return 0
    else:
        res = json.loads(response.content)
        print(res)
        if res["err"]:
            return 0
    return 1



def new_func(dir_path):
    for i in dir_path.iterdir():
        if i.is_dir():
            func(i)
        else:
            try:
                name = str(i).rsplit("/", 1)[1]
                print("name", name)
                print("*****")
                res = new_post_image(str(i), name)
                if not res:
                    print(str(i),name)
            except Exception as e:
                print(str(e))
                print(dir_path)


if __name__ == '__main__':
    func(pathlib.Path(path))
