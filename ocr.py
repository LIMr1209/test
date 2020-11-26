from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = "20346533"
API_KEY = "uL2QfGtKccfQHy3kcICG3XGX"
SECRET_KEY = "BWpsHGIW7phnPkTpE3XBmrkrkRcgxGk6"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# image = get_file_content('5c0faf06ce156a67f3915562.jpg')

# """ 调用通用文字识别（高精度版） """
# client.basicAccurate(image)
#
# """ 如果有可选参数 """
# options = {}
# options["detect_direction"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别（高精度版） """
# res = client.basicGeneralUrl('https://p4.taihuoniao.com/image/181211/5c0faf06ce156a67f3915562', options)
# print(res)
# # res = client.basicAccurate(image, options)
# level = ''
# if res['words']:
#     for i in res['words']:
#         if "& coMPETION PlATINUM A' DESIGN AWARD" in i['words']:
#             level = "Platinum A' Design Award/铂金奖"

url = "https://p4.taihuoniao.com/image/181211/5c0faf06ce156a67f3915562"

""" 调用网络图片文字识别, 图片参数为远程url图片 """
client.webImageUrl(url)

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["detect_language"] = "true"

""" 带参数调用网络图片文字识别, 图片参数为远程url图片 """
res = client.webImageUrl(url, options)
print(res)