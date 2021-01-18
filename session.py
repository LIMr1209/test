import requests


class HarborAapi(object):
    def __init__(self, auth):
        self.auth = auth

    def setting(self):
        ###定义会话保持ｓ并且设置auth属性， auth 认证会话保持
        self.session = requests.session()
        self.session.auth = self.auth

    def get_projects(self, req_url):
        header = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        r = self.session.get(req_url, headers=header)
        # print(r.text)
        print(r.status_code)

from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('thn', 'admin')

harbor = HarborAapi(auth)
harbor.setting()  ###
harbor.get_projects('http://120.132.59.206:9600/')
harbor.get_projects('http://120.132.59.206:9600/product/list?t=cat_2')
