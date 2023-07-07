import json
import time
import traceback

import requests

proxies = {
    "http": "http://10.25.10.132:7890",
    "https": "http://10.25.10.132:7890",
}

cookies = {
    'OptanonAlertBoxClosed': '2023-06-20T01:58:39.359Z',
    'OptanonConsent': 'groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
    'AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg': '1',
    'AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg': '1099438348%7CMCMID%7C17966873185549161637477475827909361091%7CMCAID%7CNONE%7CMCOPTOUT-1687233520s%7CNONE%7CvVersion%7C2.1.0',
    's_lv_s': 'Less%20than%201%20day',
    's_nr': '1687854909515-Repeat',
    's_lv': '1687854909515',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE2ODc4NTQ1MzI0MzlfMTg2NGQyOWEtMTc4MS00OGE4LTllMzQtZTlkNTQzOWQwNzQzX3V3MiIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiJtaXhhbW8xIiwidXNlcl9pZCI6IkYzODYyOTA2NjQxQkRFOUUwQTQ5NUM0QUBBZG9iZUlEIiwic3RhdGUiOiIiLCJhcyI6Imltcy1uYTEiLCJhYV9pZCI6IkYzODYyOTA2NjQxQkRFOUUwQTQ5NUM0QUBBZG9iZUlEIiwiY3RwIjowLCJmZyI6IlhSNlRaV0dCVlBQNU1QTUtVTVFWNUhBQUhFPT09PT09Iiwic2lkIjoiMTY4NzY3MjY5MjQwMV82ZmZiODBlZi05ZDg0LTQ5NTAtYjM2MS0zYjAwNWQ4NTAxMzZfdWUxIiwicnRpZCI6IjE2ODc4NTQ1MzI0MzlfN2FiMmQxNGQtZjJmZi00YzI0LTkwNWUtODc1MjU0YjFkZWNmX3V3MiIsIm1vaSI6IjY4YjA5ZDhlIiwicGJhIjoiTWVkU2VjTm9FVixMb3dTZWMiLCJydGVhIjoiMTY4OTA2NDEzMjQzOSIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNjg3ODU0NTMyNDM5Iiwic2NvcGUiOiJvcGVuaWQsQWRvYmVJRCJ9.Q2a8ROZiPJac8hubq8bfLj4NYfAc0I__EJPxxi9YNx09SBfcEenXp1xbu7PDe6apXxPpMftqg8qA9RKQqoNXpgqodsDEIIicrjJT0BCeGCE74QWIV2E5jXaGxEsc_bsTPvHAROxcg1dGgXfDDV_NAyIOGc5rfiSIL1kqKK20BRKUfB4QrLzK-MjZ1KhU0IU7fFF-YbOU_AIP-94N-kZwVRA8fGGmX8F9ECChKkeaSmlw3QRfE7MakAL6kYTMfL25O2qC-_BrZoSISXsfBbuUgM_lyxe2VLQYqsI9vxGt0Nh4oHmcQk2eiyb-fSa9-MaPsBS4d5HOXEenm_rSTAgtVw',
    'Connection': 'keep-alive',
    # 'Cookie': 'OptanonAlertBoxClosed=2023-06-20T01:58:39.359Z; OptanonConsent=groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=1099438348%7CMCMID%7C17966873185549161637477475827909361091%7CMCAID%7CNONE%7CMCOPTOUT-1687233520s%7CNONE%7CvVersion%7C2.1.0; s_lv_s=Less%20than%201%20day; s_nr=1687854909515-Repeat; s_lv=1687854909515',
    'Referer': 'https://www.mixamo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Api-Key': 'mixamo2',
    'X-Requested-With': 'XMLHttpRequest',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI0Nzc5ODkiLCJhcCI6IjE4MzQ3OTQ5NzUiLCJpZCI6ImM5ZDFlZjhiNTFlMmZmZmYiLCJ0ciI6Ijg1M2Y5MGRlMzdlYTk4ZjQwODhiOTViYjM4ODA4N2QwIiwidGkiOjE2ODc4NTQ5MjgwOTksInRrIjoiMTMyMjg0MCJ9fQ==',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'traceparent': '00-853f90de37ea98f4088b95bb388087d0-c9d1ef8b51e2ffff-01',
    'tracestate': '1322840@nr=0-1-2477989-1834794975-c9d1ef8b51e2ffff----1687854928099',
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