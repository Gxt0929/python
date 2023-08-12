# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from lxml import etree


def wyy():
    url = 'https://music.163.com/#/song?id=188261'
    driver = webdriver.Edge()
    driver.get(url)

    driver.switch_to.frame('g_iframe')

    i = 1

    with open('网易云评论.csv', 'w', encoding='utf-8-sig') as f:
        while 1:
            r = driver.page_source
            re = etree.HTML(r)
            div_list = re.xpath('//div[@class="cmmts j-flag"]/div')

            for div in div_list:
                name = div.xpath('.//a[@class="s-fc7"]/text()')[0]
                txt = div.xpath('.//div[@class="cnt f-brk"]/text()')
                if len(txt) > 1:
                    txt = txt[1]
                else:
                    txt = txt[0][1:]
                print(txt)
                nice = div.xpath('.//a[@data-type="like"]/text()')
                nice = nice[0][2:-1] if nice else '0'
                f.write(f'{name}, {txt}, {nice}\n')

            driver.execute_script('document.documentElement.scrollTo(0, 10000)')

            next_a = driver.find_element(By.LINK_TEXT, '下一页')
            if i < 10:
                next_a.click()
                i += 1
                time.sleep(1)
            else:
                 break

    driver.quit()



if __name__ == '__main__':
    wyy()