import time
from appium import webdriver

import json

if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",  # 操作系统
        "deviceName": "950c2d25",  # 设备 ID
        "platformVersion": "11",  # 设备版本号
        "appPackage": "com.tencent.mm",  # app 包名
        "appActivity": "com.tencent.mm.ui.LauncherUI",  # app 启动时主 Activity
        'noReset': True,  # 是否保留 session 信息，可以避免重新登录
        # 'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
        # 'resetKeyboard': True  # 将键盘给隐藏起来
    }
    print(json.dumps(desired_caps))
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(1)
    print('点击微信搜索框')
    driver.find_element_by_id('com.tencent.mm:id/he6').click()
    time.sleep(1)
    print('在搜索框输入搜索信息')
    driver.find_element_by_id('com.tencent.mm:id/bxz').send_keys('文件传输助手')
    time.sleep(1)
    print('点击搜索到的内容')
    driver.find_element_by_id('com.tencent.mm:id/ir3').click()
    time.sleep(1)
    # 输入文字
    ele = driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.tencent.mm:id/auj"]')
    ele.clear()
    ele.send_keys('傻逼佳栋')
    time.sleep(1)
    # 输入表情
    driver.find_element_by_id('com.tencent.mm:id/ay9').click()
    time.sleep(1)
    driver.find_element_by_xpath('(//com.tencent.mm.ui.MMImageView[@content-desc="[微笑]"])[1]').click()
    # 点击发送按钮发送信息
    driver.find_element_by_id('com.tencent.mm:id/ay5').click()
    # 退出
    # driver.quit()

