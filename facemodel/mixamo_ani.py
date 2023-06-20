import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumSpider:

    def __init__(self, *args, **kwargs):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # 初始化chrome对象
        # google - chrome - stable - -remote - debugging - port = 9222 - -user - data - dir = "/home/limr/extra_chrome"
        self.browser = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.browser, 30)  # 指定元素加载超时时间

    def start(self):
        base_dir = "/home/limr/Desktop/model/女_fbx"
        for i in os.listdir(base_dir):
            path = os.path.join(base_dir,i)
            while True:
                try:
                    upload_button = self.browser.find_element(By.XPATH,
                                                              '//*[@id="site"]/div[3]/div/div/div[2]/div/div[2]/div[2]/div[1]/button[3]')
                    upload_button.click()
                    break
                except:
                    time.sleep(2)
                    continue
            elem = WebDriverWait(self.browser, 30, 0.5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="file"]')
                )
            )
            file_input = self.browser.find_element(By.XPATH, '//*[@id="file"]')
            file_input.send_keys(path)

            elem = WebDriverWait(self.browser, 30, 0.5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="autorigger"]')
                )
            )

            elem = WebDriverWait(self.browser, 30, 0.5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="autorig-holder"]//div[@class="modal-footer"]/button[not(@disabled)]')
                )
            )


            next_button = self.browser.find_element(By.XPATH, '//div[@class="autorig-holder"]//div[@class="modal-footer"]/button')
            next_button.click()

            download_button = self.browser.find_element(By.XPATH, '//*[@id="site"]/div[3]/div/div/div[2]/div/div[2]/div[2]/div[1]/button[1]')
            download_button.click()
            elem = WebDriverWait(self.browser, 30, 0.5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="modal-dialog"]//div[@class="modal-footer"]/div/button[2]')
                )
            )
            download_o_button = self.browser.find_element(By.XPATH, '//div[@class="modal-dialog"]//div[@class="modal-footer"]/div/button[2]')
            download_o_button.click()
            while True:
                if os.path.exists("/home/limr/Downloads/Idle.fbx"):
                    print("处理结束", i)
                    os.rename("/home/limr/Downloads/Idle.fbx", f"/home/limr/Downloads/{i}")
                    break
                else:
                    continue




if __name__ == '__main__':
    test = SeleniumSpider()
    test.start()