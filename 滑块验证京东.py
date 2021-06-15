import asyncio
import random
import cv2
from pyppeteer import launch, connect
from urllib import request


# 滑块的缺口距离识别
async def get_distance():
    img = cv2.imread('image.png', 0)
    template = cv2.imread('template.png', 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
    value = cv2.minMaxLoc(res)[2][0]
    distance = value * 278/360
    return distance


async def main():
    # browser = await launch({
    #     'headless': False,
    #     'args': ['--no-sandbox', '--window-size=1366,768'],
    # })
    # browserWSEndpoint 获取chrome debug 端口
    # http://127.0.0.1:端口/json/version
    connect_params = {
        'browserWSEndpoint': 'ws://127.0.0.1:9222/devtools/browser/e4c8d886-0c0b-46db-b04b-98eb8f008afa',
        'logLevel': 3,
    }
    browser = await connect(connect_params)
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.goto('https://passport.jd.com/login.aspx')
    await page.waitFor(1000)
    await page.click('div.login-tab-r')
    await page.waitFor(1000)
    # 模拟人工输入用户名、密码
    await page.type('#loginname', '123456789@163.com',
                    {'delay': random.randint(60, 121)})
    await page.type('#nloginpwd', '1234567890',
                    {'delay': random.randint(100, 151)})
    await page.waitFor(2000)
    await page.click('div.login-btn')
    await page.waitFor(3000)
    # 模拟人工拖动滑块、失败则重试
    while True:
        if await page.J('#ttbar-login'):
            print('登录成功！')
            await page.waitFor(6000)
            break
        else:
            image_src = await page.Jeval('.JDJRV-bigimg >img', 'el => el.src')
            request.urlretrieve(image_src, 'image.png')
            template_src = await page.Jeval('.JDJRV-smallimg >img', 'el => el.src')
            request.urlretrieve(template_src, 'template.png')
            await page.waitFor(3000)
            el = await page.J('div.JDJRV-slide-btn')
            box = await el.boundingBox()
            await page.hover('div.JDJRV-slide-btn')
            distance = await get_distance()
            await page.mouse.down()
            await page.mouse.move(box['x'] + distance + random.uniform(30, 33), box['y'], {'steps': 30})
            await page.waitFor(random.randint(300, 700))
            await page.mouse.move(box['x'] + distance + 29, box['y'], {'steps': 30})
            await page.mouse.up()
            await page.waitFor(3000)


asyncio.get_event_loop().run_until_complete(main())
