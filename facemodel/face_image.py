import json
import requests
import pathlib
import pdb
import re

path = "/home/limr/Downloads/0602演示图片"

base_url = "http://10.25.20.11:8000"

def post_image(filepath, name, cue_word):
    response = requests.post(url="{}/admin/face_image_auto/save".format(base_url), files={'file': open(filepath, 'rb')},
                             data={"name": name, "cue_word": cue_word}, headers={"cookie":"session=1533a956-45b1-4da2-9a5e-eaa19fbe428a.6fapPl8jsS1012WwIlCl7PFwQKQ"})
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
                             data={"name": name}, headers={"cookie":"session=1533a956-45b1-4da2-9a5e-eaa19fbe428a.6fapPl8jsS1012WwIlCl7PFwQKQ"})
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
    new_func(pathlib.Path(path))
