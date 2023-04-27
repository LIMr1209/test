import json
import requests
import pathlib

path = "2222"

base_url = "http://10.25.20.15:8007"

def post_image(filepath, name, cue_word):
    response = requests.post(url="{}/admin/face_image_auto/save".format(base_url), files={'file': open(filepath, 'rb')},
                             data={"name": name, "cue_word": cue_word}, headers={"cookie":"session=0ab9df15-a5b0-44a4-89be-4623fcbbc5b3.L72uF5FGaDd4528BkP78Gj_hIbU"})
    if response.status_code != 200:
        return 0
    else:
        res = json.loads(response.content)
        if res["err"]:
            return 0
    return 1


def func(dir_path):
    for i in dir_path.iterdir():
        if i.is_dir():
            func(i)
        else:
            try:
                dir_name = str(dir_path).rsplit("\\", 1)[1]
                name = dir_name.split("，", 1)[0]
                try:
                    cue_word = dir_name.split("，", 1)[1]
                except:
                    cue_word = ""
                print(i)
                print(name)
                print(cue_word)
                print("*****")
                res = post_image(str(i), name, cue_word)
                if not res:
                    print(str(i), name, cue_word)
            except:
                print(dir_path)


if __name__ == '__main__':
    func(pathlib.Path(path))
