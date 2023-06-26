import json
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
    's_lv_s': 'Less%20than%207%20days',
    's_nr': '1687673362101-Repeat',
    's_lv': '1687673362102',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE2ODc2NzMxMTc4NjFfNWE5ZDRhOWQtYjJkMS00ZjNiLTk0ODEtYjUwODU4YTVkZDI1X3V3MiIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiJtaXhhbW8xIiwidXNlcl9pZCI6IkYzODYyOTA2NjQxQkRFOUUwQTQ5NUM0QUBBZG9iZUlEIiwic3RhdGUiOiIiLCJhcyI6Imltcy1uYTEiLCJhYV9pZCI6IkYzODYyOTA2NjQxQkRFOUUwQTQ5NUM0QUBBZG9iZUlEIiwiY3RwIjowLCJmZyI6IlhSWVcyR1lEVlBQNU1QTUtVTVFWNUhBQUhFPT09PT09Iiwic2lkIjoiMTY4NzY3MzExNDM3M180ZjJjNDhjYy1kYTg0LTQyM2ItYWVkNy02NTllZmE4YjYzYWJfdWUxIiwicnRpZCI6IjE2ODc2NzMxMTc4NjJfYmViMWRjZjItNzQzNy00N2UzLWE5NDItMTI0YTE0OWNiNTA5X3V3MiIsIm1vaSI6ImEyMDFkNTdlIiwicGJhIjoiTWVkU2VjTm9FVixMb3dTZWMiLCJydGVhIjoiMTY4ODg4MjcxNzg2MiIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNjg3NjczMTE3ODYxIiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.LI7S52_-Ztk_NT3-cG6XiDX_WT-MBFZOfGWiybN_f4JMlkZiW9AZQxfNyVaIon7zpIUeVRE_o-o3EioR0Pj7fIsQPCqqLWBFccVaW252m9UPMmpJnA1TlUxwDCuvLiV1S2HoidX4pdP9Syk-IjXmUWoFu3PFJhZdxT1DBEg_qoJVWVXaiwjtNIeQI-hmyk4A9CQRyPjwhoPOA0G5e9WhdKoGsqhObdz9TOSSnEBQvWT3f311Y0OXEiGew9_6QZvoIrG6a0vOdMChlA5IIkeVyenWCwJfkxeDZ1TgUDAZWjpI8NWW6tQMoONqLlHJmQ2xpZ8Tpmt2cdMATZjA0y1miQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'OptanonAlertBoxClosed=2023-06-20T02:30:24.824Z; OptanonConsent=groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=1099438348%7CMCMID%7C91307366737064012929105513548722826897%7CMCAID%7CNONE%7CMCOPTOUT-1687235425s%7CNONE%7CvVersion%7C2.1.0; s_lv_s=Less%20than%207%20days; s_nr=1687673362101-Repeat; s_lv=1687673362102',
    'If-None-Match': 'W/"9b29e9e0ef70b1038fb5c1a570216c4a"',
    'Referer': 'https://www.mixamo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Api-Key': 'mixamo2',
    'X-Requested-With': 'XMLHttpRequest',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI0Nzc5ODkiLCJhcCI6IjE4MzQ3OTQ5NzUiLCJpZCI6IjQ1NTdiNGU1YTAxMWVlNTIiLCJ0ciI6IjdkMjZhNWM5NTVmOTcxNThjM2VlZjNjZWZlNGUxYmIwIiwidGkiOjE2ODc2NzMzNjIxMTIsInRrIjoiMTMyMjg0MCJ9fQ==',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'traceparent': '00-7d26a5c955f97158c3eef3cefe4e1bb0-4557b4e5a011ee52-01',
    'tracestate': '1322840@nr=0-1-2477989-1834794975-4557b4e5a011ee52----1687673362112',
}

page = 17

params = {
    'page': '1',
    'limit': '48',
    'order': '',
    'type': 'Motion,MotionPack',
    'query': '',
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
            params = {
                'similar': '0',
                'character_id': 'afb26de1-7840-4da5-848b-07c3c7179ac8',
            }
            motion_id = i["motion_id"]
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
                    'character_id': 'afb26de1-7840-4da5-848b-07c3c7179ac8',
                    'retargeting_payload': '',
                    'target_type': 'skin',
                }
                name = rf'{motion_id}+$+{i["name"]}.txt'.replace("/","\\")

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
                with open(f"ani/{name}", "w") as f:
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
                        'character_id': 'afb26de1-7840-4da5-848b-07c3c7179ac8',
                        'retargeting_payload': '',
                        'target_type': 'skin',
                    }
                    name = f'{motion_id}+$+{i["name"]}+index+{num}.txt'.replace("/","\\")

                    print("结合模型和动画获取结果")
                    response = requests.post('https://www.mixamo.com/api/v1/animations/stream', cookies=cookies,
                                             headers=headers,
                                             json=json_data, proxies=proxies)
                    if response.status_code != 200:
                        raise Exception("500")
                    # if os.path.exists(f"ani/{name}"):
                    #     raise Exception("已经存在该文件")
                    with open(f"ani/{name}", "w") as f:
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
    except Exception as e:
        traceback.print_exc()
        print(page)
        print(motion_id)
        break