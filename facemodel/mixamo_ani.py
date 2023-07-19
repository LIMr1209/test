import json
import os.path
import time
import traceback

import requests

proxies = {
    "http": "http://10.25.10.132:7890",
    "https": "http://10.25.10.132:7890",
}

cookies = {
    'OptanonAlertBoxClosed': '2023-06-20T02:30:24.824Z',
    'OptanonConsent': 'groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
    'AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg': '1099438348%7CMCMID%7C91307366737064012929105513548722826897%7CMCAID%7CNONE%7CMCOPTOUT-1687235425s%7CNONE%7CvVersion%7C2.1.0',
    's_lv_s': 'More%20than%207%20days',
    's_nr': '1688969726530-Repeat',
    's_lv': '1688969726531',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE2ODg5Njk2Njg5MTNfZmYzMTI5ZTAtMjU4Zi00MmM3LWJjYTUtNmEwMWY1YjBmOTM4X3V3MiIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiJtaXhhbW8xIiwidXNlcl9pZCI6IkZCMTIyQ0Y4NjIxNDgwNkUwQTQ5NUM2RkBBZG9iZUlEIiwic3RhdGUiOiIiLCJhcyI6Imltcy1uYTEiLCJhYV9pZCI6IkZCMTIyQ0Y4NjIxNDgwNkUwQTQ5NUM2RkBBZG9iZUlEIiwiY3RwIjowLCJmZyI6IlhUQzVNSzZDVlBQNTRQTUtXTVFWNUhBQVNNPT09PT09Iiwic2lkIjoiMTY4ODk2OTY2NDA2MV9hMGM0NWRkNS1mM2RlLTRhOGUtODVkNC1jNmQwY2JkMzRhY2RfdWUxIiwicnRpZCI6IjE2ODg5Njk2Njg5MTRfOTBkNmJmYWItM2E1MC00Yzg5LThlNTUtNzZjYjZmZTE2NzI0X3V3MiIsIm1vaSI6IjNlYTRmMTE0IiwicGJhIjoiTWVkU2VjTm9FVixMb3dTZWMiLCJydGVhIjoiMTY5MDE3OTI2ODkxNCIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsInNjb3BlIjoib3BlbmlkLEFkb2JlSUQiLCJjcmVhdGVkX2F0IjoiMTY4ODk2OTY2ODkxMyJ9.fHQZn_JPT6-Nn9KWIshUzaO5rtmPFTfb886_JmhkO-4Ht__-7TmjuskEO3V2dctU7xCLlqaY7yBNgqwbEM12x-Z_Uc1_NZLWDZGrvJIo7F_xv2vTen-bprwZ2A7UXIYsHo_Om-zTuPI1ZTfpHE2T_ehVt_b3FRSviNWPXyk1PDfGZIwLjmY__PsRGoaImES3WX4P5rcKIU2zqeNF6CqFb0pUXRxzhTO1NW_aXuK4QunxhnSmu-e80aakHSTi0CIc5PU_tw5M0emtVaTRKfOE1-gUAuCHAtvt-QRCTiuJYsSYGmA8F8l4D2Ey_xGHmpt4PpGDtqzvcthiEaY0iOjuLQ',
    'Connection': 'keep-alive',
    'Content-type': 'application/json',
    # 'Cookie': 'OptanonAlertBoxClosed=2023-06-20T02:30:24.824Z; OptanonConsent=groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=1099438348%7CMCMID%7C91307366737064012929105513548722826897%7CMCAID%7CNONE%7CMCOPTOUT-1687235425s%7CNONE%7CvVersion%7C2.1.0; s_lv_s=More%20than%207%20days; s_nr=1688969726530-Repeat; s_lv=1688969726531',
    'Origin': 'https://www.mixamo.com',
    'Referer': 'https://www.mixamo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Api-Key': 'mixamo2',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI0Nzc5ODkiLCJhcCI6IjE4MzQ3OTQ5NzUiLCJpZCI6IjlhMjUyMDZiZTAwYTY4ZGEiLCJ0ciI6Ijk4ZDZhNmEyYmQyNDkzZjIyYTA4YWIzNDA1OTUyOTYwIiwidGkiOjE2ODg5Njk3Mjk1ODAsInRrIjoiMTMyMjg0MCJ9fQ==',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'traceparent': '00-98d6a6a2bd2493f22a08ab3405952960-9a25206be00a68da-01',
    'tracestate': '1322840@nr=0-1-2477989-1834794975-9a25206be00a68da----1688969729580',
}

keyword = ""
base_dir = "ani"
if keyword:
    base_dir = keyword



character_id = "c78dded4-b5f3-44bb-9e9f-d0adda949ea0"
page = 1

params = {
    'page': '1',
    'limit': '48',
    'order': '',
    'type': 'Motion,MotionPack',
    'query': keyword,
}

while True:
    try:
        print(f"开始爬取第{page}页")
        params["page"] = page
        try:
            page_response = requests.get('https://www.mixamo.com/api/v1/products', params=params, cookies=cookies,
                                         headers=headers, proxies=proxies)
        except:
            time.sleep(5)
            page_response = requests.get('https://www.mixamo.com/api/v1/products', params=params, cookies=cookies,
                                         headers=headers, proxies=proxies)

        print(f"请求{page}页动画")
        page_res = json.loads(page_response.content.decode("utf-8"))

        for i in page_res["results"]:
            if keyword:
                if i["name"] != keyword:
                    continue
            params = {
                'similar': '0',
                'character_id': character_id
            }
            dir_s = f"{base_dir}/"+i["motion_id"]
            if not os.path.exists(dir_s):
                os.makedirs(dir_s)
            motion_id = i["motion_id"]

            print("获取封面图")
            try:
                response = requests.get(i['thumbnail'], cookies=cookies, headers=headers, proxies=proxies)
            except:
                time.sleep(3)
                response = requests.get(i['thumbnail'], cookies=cookies, headers=headers, proxies=proxies)
            with open(f"{dir_s}/static.png", "wb") as f:
                f.write(response.content)
            try:
                response = requests.get(i['thumbnail_animated'], cookies=cookies, headers=headers, proxies=proxies)
            except:
                time.sleep(3)
                response = requests.get(i['thumbnail_animated'], cookies=cookies, headers=headers, proxies=proxies)
            with open(f"{dir_s}/animated.gif", "wb") as f:
                f.write(response.content)
            try:
                adjust_response = requests.get(
                    'https://www.mixamo.com/api/v1/products/' + motion_id,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    proxies=proxies
                )
            except:
                time.sleep(5)
                adjust_response = requests.get(
                    'https://www.mixamo.com/api/v1/products/' + motion_id,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    proxies=proxies
                )

            print(f"获取动画详情数据{motion_id}")
            adjust_res = json.loads(adjust_response.content.decode("utf-8"))

            ani_headers = headers.copy()
            ani_headers["Accept"] = "*/*"
            if "gms_hash" in adjust_res["details"]:
                temp = adjust_res["details"]["gms_hash"]
                data = []
                for j in temp["params"]:
                    data.append(str(j[1]))
                temp["params"] = ",".join(data)
                json_data = {
                    'gms_hash': [temp],
                    'character_id': character_id,
                    'retargeting_payload': '',
                    'target_type': 'skin',
                }
                name = rf'{i["name"]}.txt'.replace("/","\\")

                print("结合模型和动画获取结果")
                try:
                    response = requests.post('https://www.mixamo.com/api/v1/animations/stream', cookies=cookies,
                                             headers=headers,
                                             json=json_data, proxies=proxies)
                except:
                    time.sleep(5)
                    response = requests.post('https://www.mixamo.com/api/v1/animations/stream', cookies=cookies,
                                             headers=headers,
                                             json=json_data, proxies=proxies)
                if response.status_code != 200:
                    raise Exception("500")
                # if os.path.exists(f"ani/{name}"):
                #     raise Exception("已经存在该文件")
                with open(f"{dir_s}/{name}", "w") as f:
                    f.write(response.content.decode("utf-8"))
                print(f"结果保存{name}")
                print("*" * 10)
            elif "motions" in adjust_res["details"]:
                for num, x in enumerate(adjust_res["details"]["motions"]):
                    temp = x["gms_hash"]
                    data = []
                    for j in temp["params"]:
                        data.append(str(j[1]))
                    temp["params"] = ",".join(data)
                    json_data = {
                        'gms_hash': [temp],
                        'character_id': character_id,
                        'retargeting_payload': '',
                        'target_type': 'skin',
                    }
                    name = f'{i["name"]}+index+{num}.txt'.replace("/","\\")

                    print("结合模型和动画获取结果")
                    response = requests.post('https://www.mixamo.com/api/v1/animations/stream', cookies=cookies,
                                             headers=headers,
                                             json=json_data, proxies=proxies)
                    if response.status_code != 200:
                        raise Exception("500")
                    # if os.path.exists(f"ani/{name}"):
                    #     raise Exception("已经存在该文件")
                    with open(f"{dir_s}/{name}", "w") as f:
                        f.write(response.content.decode("utf-8"))
                    print(f"结果保存{name}")
                    print("*" * 10)
            else:
                raise Exception("未识别动画")

        print("-" * 10)
        if page < page_res["pagination"]["num_pages"]:
            page += 1
        else:
            break
        if keyword:
            break
    except Exception as e:
        traceback.print_exc()
        print(page)
        print(motion_id)
        break