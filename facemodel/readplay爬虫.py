import json

import requests

cookies = {
    '_gcl_au': '1.1.383380653.1685016990',
    '_rdt_uuid': '1685016991235.6572f645-678a-47fe-a135-a0dfd39581d2',
    'hubspotutk': '1d1fb8b90c4501d4c971cd0157657e5d',
    '__hssrc': '1',
    '_hjSessionUser_2040154': 'eyJpZCI6IjU1ZWViMmQ3LWQyZmMtNTIxZC05ZTcwLWFlNjIwMjgxMDJjZSIsImNyZWF0ZWQiOjE2ODUwMTY5OTA4MTcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.1459856245.1686819611',
    'ln_or': 'eyIzMTA1NzYxIjoiZCJ9',
    '_hjIncludedInSessionSample_2040154': '0',
    '_hjSession_2040154': 'eyJpZCI6ImQwMjllMDkyLWI1ZmQtNGIwZi04YmVlLWE0NzVmNjE1M2I0NyIsImNyZWF0ZWQiOjE2ODY4MjM5Mzc2MjEsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '1',
    '__hstc': '48581945.1d1fb8b90c4501d4c971cd0157657e5d.1685016993375.1686819613623.1686823939388.5',
    'amp_8bc7fa': 'tvJJ8XyfXMDHltDe1zr7lt...1h2v8lek1.1h2v8np6c.3.0.3',
    '_ga_FHTLT07QH0': 'GS1.1.1686822695.5.1.1686824019.59.0.0',
    '_ga': 'GA1.2.838605304.1685016991',
    '_gat_gtag_UA_165056853_1': '1',
    '_gat_UA-165056853-1': '1',
    '__hssc': '48581945.3.1686823939388',
    'amp_8bc7fa_readyplayer.me': 'tvJJ8XyfXMDHltDe1zr7lt...1h2v8les7.1h2v8o3q2.13.iv.k2',
}

headers = {
    'authority': 'readyplayer.me',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc0Fub255bW91cyI6dHJ1ZSwidXNlcklkIjoiNjQ2ZjUxOWU1NTIzMGI0YzFiYWUwMzlhIiwiYWJpbGl0eSI6W1sibWFuYWdlIiwiQXZhdGFyIix7InVzZXJJZCI6IjY0NmY1MTllNTUyMzBiNGMxYmFlMDM5YSJ9XSxbIm1hbmFnZSIsIlVzZXIiLHsiX2lkIjoiNjQ2ZjUxOWU1NTIzMGI0YzFiYWUwMzlhIn1dLFsicmVhZCIsIlBhcnRuZXIiXSxbInJlYWQsY3JlYXRlIiwiT3JnYW5pemF0aW9uIl0sWyJyZWFkIiwiQXBwbGljYXRpb24iXSxbInJlYWQsdXNlIiwiQXNzZXQiLHsibG9ja2VkIjp7IiRuZSI6dHJ1ZX19XSxbInJlYWQsdXNlIiwiQXNzZXQiLHsiaWQiOnt9fV0sWyJyZWFkLHVzZSIsIkFzc2V0Iix7Imdyb3Vwcy5pZCI6e319XSxbInBvc3QiLCJXZWJob29rRXZlbnQiLHsicm91dGluZ0tleSI6InN0dWRpby11aS52MS5nZXR0aW5nLXN0YXJ0ZWQuY29tcGxldGVkIn1dXSwiaWF0IjoxNjg1MDE2OTkwfQ.VXZDLkZ6kh4SaKOgoGHd3LGruOsUKBXMqPwMBtmvxIw',
    # 'cookie': '_gcl_au=1.1.383380653.1685016990; _rdt_uuid=1685016991235.6572f645-678a-47fe-a135-a0dfd39581d2; hubspotutk=1d1fb8b90c4501d4c971cd0157657e5d; __hssrc=1; _hjSessionUser_2040154=eyJpZCI6IjU1ZWViMmQ3LWQyZmMtNTIxZC05ZTcwLWFlNjIwMjgxMDJjZSIsImNyZWF0ZWQiOjE2ODUwMTY5OTA4MTcsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1459856245.1686819611; ln_or=eyIzMTA1NzYxIjoiZCJ9; _hjIncludedInSessionSample_2040154=0; _hjSession_2040154=eyJpZCI6ImQwMjllMDkyLWI1ZmQtNGIwZi04YmVlLWE0NzVmNjE1M2I0NyIsImNyZWF0ZWQiOjE2ODY4MjM5Mzc2MjEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; __hstc=48581945.1d1fb8b90c4501d4c971cd0157657e5d.1685016993375.1686819613623.1686823939388.5; amp_8bc7fa=tvJJ8XyfXMDHltDe1zr7lt...1h2v8lek1.1h2v8np6c.3.0.3; _ga_FHTLT07QH0=GS1.1.1686822695.5.1.1686824019.59.0.0; _ga=GA1.2.838605304.1685016991; _gat_gtag_UA_165056853_1=1; _gat_UA-165056853-1=1; __hssc=48581945.3.1686823939388; amp_8bc7fa_readyplayer.me=tvJJ8XyfXMDHltDe1zr7lt...1h2v8les7.1h2v8o3q2.13.iv.k2',
    'referer': 'https://readyplayer.me/avatar',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'app': 'default',
}
import pathlib
response = requests.get('https://readyplayer.me/api/assets', params=params, cookies=cookies, headers=headers)

data = json.loads(response.content.decode("utf-8"))
# data = data[:1]


path = "readyplayer"
total = len(data)
num = 0
for i in data:
    print("进度", num / total)
    num += 1
    print(i["gender"])
    print(i["assetType"])
    gender = i["gender"]
    if not gender:
        glb_path = f"中性/{i['assetType']}/模型"
        png_path = f"中性/{i['assetType']}/图片"
    elif gender == "male":
        glb_path = f"男/{i['assetType']}/模型"
        png_path = f"男/{i['assetType']}/图片"
    else:
        glb_path = f"女/{i['assetType']}/模型"
        png_path = f"女/{i['assetType']}/图片"
    if "icon" not in i:
        continue
    png_url = i["icon"].replace("?w=64", "")
    if "model" not in i:
        continue
    model_url = i["model"]
    file_name = model_url.rsplit("/",1)[1].rsplit(".",1)[0]
    glb_path = pathlib.Path(path, glb_path)
    png_path = pathlib.Path(path, png_path)
    if not glb_path.exists():
        glb_path.mkdir(exist_ok=True, parents=True)
    if not png_path.exists():
        png_path.mkdir(exist_ok=True, parents=True)
    glb_response = requests.get(model_url)
    with open(pathlib.Path(glb_path, f"{file_name}.glb"), "wb") as f:
        f.write(glb_response.content)

    png_response = requests.get(png_url)
    with open(pathlib.Path(png_path, f"{file_name}.png"), "wb") as f:
        f.write(png_response.content)

