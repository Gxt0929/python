# -*- coding: utf-8 -*-
import time
import xlwt

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from lxml import etree

def douyin():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(
        'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35')
    driver = webdriver.Edge(options=options)

    url = 'https://www.douyin.com/user/MS4wLjABAAAA6QIRfJADgoyzikxITn4r6GsUVINB-EiR4UOY_ju1AU2W5Fq4YAkj-2n33_fK_gca?vid=7154044222864215331'

    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    writebook = xlwt.Workbook(encoding='utf-8')
    sheet1 = writebook.add_sheet('Sheet1', cell_overwrite_ok=True)
    sheet1.write(0, 0, '视频名称')
    sheet1.write(0, 1, '点赞数')
    sheet1.write(0, 2, '视频地址')
    for i in range(10):
        driver.execute_script('document.documentElement.scrollTo(0, 10000)')
        time.sleep(1)

    sor = driver.page_source
    r = etree.HTML(sor)
    li_list = r.xpath('//ul[@class="EZC0YBrG"]/li')
    name = r.xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[1]/h1/span/span/span/span/span/span/text()')[0]
    # print(name)
    fs = r.xpath('.//div[@class="TxoC9G6_"]/text()')[1]
    print(fs)

    i = 1
    for li in li_list:
        pl = li.xpath('.//p[@class="__0w4MvO"]/text()')[0]
        # print(pl)
        nice = li.xpath('.//span[contains(@class, "author-card-user-video-like")]/span/text()')[0]
        # print(nice)
        src = li.xpath('.//div/a/@href')[0]
        # print(src)
        j = 0
        sheet1.write(i, j, pl)
        j += 1
        sheet1.write(i, j, nice)
        j += 1
        sheet1.write(i, j, src)
        i += 1
        writebook.save('douyin.xls')
if __name__ == '__main__':
    douyin()