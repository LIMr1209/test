import os
import requests

def req(url, num, file_name, file_path):
    with open(file_path, 'rb') as f:
        contents = f.read()

    payload={'num': num}
    file_tuple = (file_name, contents, 'audio/wav')
    files = {'fileb': file_tuple}
    response = requests.post(url, data=payload, files=files)

    return response


if __name__ == '__main__':

    num= '2'  # 1：dyx(段艺璇)， 2：yyq（袁一琦）
    url = 'http://10.25.10.38:1146/wav2wav'
    file_path = 'syz_79.wav'
    file_name  = os.path.basename(file_path)
    response = req(url, num, file_name, file_path)
    with open(file_name, 'wb') as f:
        f.write(response.content)


