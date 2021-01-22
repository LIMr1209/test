import random
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


def input_account_password(browser):
    # Waiting for loading done. click password login
    browser.find_element_by_xpath('//div[@active-tab="1"]').click()
    time.sleep(3)
    act = "//input[@id='mobile']"
    pwd = "//input[@id='password']"
    btn = "//div[@class='sign-in']/div[2]/div[4]"
    browser.find_element_by_xpath(act).send_keys('mobile')
    browser.find_element_by_xpath(pwd).send_keys('password')
    browser.find_element_by_xpath(btn).click()
    time.sleep(2)
    # Waiting for loading and enter account&password
    elem = WebDriverWait(browser, 20, 0.5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'gt_popup_wrap')
        )
    )
    if not elem.is_displayed():
        browser.find_element_by_xpath(btn).click()
    time.sleep(2)


def capture_screenshots(browser):
    # Intercept verification code picture
    filename1 = 'temp/fullpage1.png'
    browser.get_screenshot_as_file(filename1)
    area = browser.find_element_by_xpath('//a[@class="gt_bg gt_show"]')

    left = area.location['x']
    top = area.location['y']
    right = left + area.size['width']
    bottom = top + area.size['height']
    print(left, top, right, bottom)

    browser.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]').click()
    time.sleep(5)
    filename2 = 'temp/fullpage2.png'
    browser.get_screenshot_as_file(filename2)

    picture1 = Image.open(filename1).crop((left, top, right, bottom))
    picture2 = Image.open(filename2).crop((left, top, right, bottom))
    picture1.save('temp/crop1.png')
    picture2.save('temp/crop2.png')
    return picture1, picture2


def gap_offset(picture1, picture2, start=0, threhold=60):
    # Get the gap offset in the verification code picture
    coordinate = list()
    # 比较图片 获取rgb 值 阈值超过 60 的 x
    for x in range(start, picture1.size[0]):
        for y in range(picture1.size[1]):
            rgb1 = picture1.load()[x, y]
            rgb2 = picture2.load()[x, y]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 <
                    threhold):
                coordinate.append(x)
    coordinate = list(set(coordinate))
    try:
        # 滑块的开始位置
        start = coordinate[0]
        # 缺失位置的开始位置为 未链接（>2）x列表的第一个
        end = [c for c in coordinate if c -
               coordinate[coordinate.index(c) - 1] > 2][0]
        offset = end - start
    except Exception as e:
        offset = int(sum(coordinate) / len(coordinate))
    # 偏移量
    return offset


def slide_tracks(distance):
    # Computational simulation of notch sliding trajectory
    distance += 20  # 偏移位置增加20个像素（超过目标20个像素）
    v, t, current = [0, 0.3, 0]
    forward_tracks = []
    middle = distance * 3 / 5
    while current < distance:
        if current < middle:
            a = 4
        else:
            a = -5
        s = v * t + (1 / 2) * a * (t ** 2)  # 偏移量
        v = v + a * t  # 速度
        current += s
        forward_tracks.append(round(s))
        t += 0.05
    back_tracks = [-4, -4, -3, -3, -2, -2, -1, -1]  # 超过20 个像素 重新移动回来
    # 补全差异
    diff_value = sum(forward_tracks) - distance
    if diff_value > 0:
        back_tracks.append(-diff_value)
    return forward_tracks, sorted(back_tracks)


def drag_slider(browser, forward_tracks, back_tracks):
    button = browser.find_element_by_css_selector('.gt_slider_knob.gt_show')
    ActionChains(browser).click_and_hold(button).perform()  # 点击
    time.sleep(random.randint(5, 10) / 10)
    # 向后移动
    for ft in forward_tracks:
        ActionChains(browser).move_by_offset(xoffset=ft,
                                             yoffset=0).perform()
    time.sleep(random.randint(8, 12) / 10)
    # 像前移动
    for bt in back_tracks:
        ActionChains(browser).move_by_offset(xoffset=bt,
                                             yoffset=0).perform()
    time.sleep(random.randint(5, 10) / 10)
    ActionChains(browser).release(button).perform()  # 释放鼠标
    time.sleep(1)


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://www.tianyancha.com/login')
# Enter account passord and click login
input_account_password(browser)

# Get the verification code picture and calculate the gap offset
picture1, picture2 = capture_screenshots(browser)
offset = gap_offset(picture1, picture2)
print(offset)

# Calculating the sliding trajectory and move slider
forward_tracks, back_tracks = slide_tracks(offset)
drag_slider(browser, forward_tracks, back_tracks)
time.sleep(5)
browser.get_screenshot_as_file('temp/login_after.png')
