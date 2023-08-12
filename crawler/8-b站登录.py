# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

from pachong.chaojiying import Chaojiying_Client


def bili():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35')


    driver = webdriver.Edge(options=options)

    url = 'https://www.bilibili.com/'
    driver.get(url)

    driver.find_element(By.XPATH, '//div[@class="header-login-entry"]').click()
    time.sleep(1)
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//form[@class="tab__form"]/div[1]/input').send_keys('13339681690')
    driver.find_element(By.XPATH, '//form[@class="tab__form"]/div[3]/input').send_keys('guo22917')
    driver.find_element(By.XPATH, '//div[@class="btn_primary "]').click()
    time.sleep(1)

    verify_code = driver.find_element(By.XPATH, '//div[@class="geetest_panel_box geetest_panelshowclick"]')
    print(verify_code)
    verify_code.screenshot('code.png')

    chaojiying = Chaojiying_Client('160837538', 'guo22917', '948104')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 9004))

    pic_str = chaojiying.PostPic(im, 9004)['pic_str']
    pic_list = pic_str.split('|')
    print(pic_list)
    action = ActionChains(driver)
    while 1:
        for pic in pic_list:
            x = pic.split(',')[0]
            y = pic.split(',')[1]
            print(x, y)
            action.move_to_element_with_offset(verify_code, x, y).click().perform()
            time.sleep(0.5)

        driver.find_element(By.XPATH, '//div[@class="geetest_commit_tip"]').click()


if __name__ == '__main__':
    bili()
