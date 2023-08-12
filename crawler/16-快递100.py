# -*- coding: utf-8 -*-
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_url():
    url = 'https://www.kuaidi100.com/network/'
    return url


def file_wirte(f):
    # 获取网页动态源码
    # 获取数据并写入文件
    r = etree.HTML(driver.page_source)
    div_list = r.xpath('//div[@class="network-list"]/dl')
    for dl in div_list:
        last_name = dl.xpath('string(./dt/a)')
        last_name = last_name.replace('\r', '').replace('\t', '').replace('\n\n', '\n').replace('\xa0', ' ')
        address = dl.xpath('./dd[1]/text()')[0][5:]
        if len(dl.xpath('./dd[2]/text()')) == 0:
            contact_num = dl.xpath('./dd[2]/text()')
        else:
            contact_num = dl.xpath('./dd[2]/text()')[0][5:]
        if len(dl.xpath('./dd[4]/dl/dd[1]/text()')) == 0:
            give_address = dl.xpath('./dd[4]/dl/dd[1]/text()')
        else:
            give_address = dl.xpath('./dd[4]/dl/dd[1]/text()')[0]
        if len(dl.xpath('./dd[4]/dl/dt[2]/text()')) == 0:
            dont_give_address = dl.xpath('./dd[4]/dl/dd[2]/text()')
        else:
            dont_give_address = dl.xpath('./dd[4]/dl/dd[2]/text()')[0]
        f.write(f'{last_name},{address}, {contact_num}, {give_address}, {dont_give_address}\n')
        print('正在获取中...')


def kd_write(li_d, key):
    # 模拟点击事件
    with open(f'{key}-{li_d}.csv', 'w', encoding='utf-8') as f:
        f.write(f'{"公司名字"},{"地址"}, {"联系电话"}, {"派送范围"}, {"不派送范围"}\n')
        a = driver.find_element(By.XPATH, f'//ul[@id="companyCount"]/li/a[text()="{li_d}"]')
        driver.execute_script("arguments[0].click();", a)
        try:
            while 1:
                driver.execute_script('document.documentElement.scrollTo(0, 10000)')
                time.sleep(1)
                file_wirte(f)
                driver.find_element(By.XPATH, '//div[@id="pager"]/b[@class="page-down-active"]').click()
        except Exception:
            return 1


def kd100(key):
    # 模拟输入并找到相应的快递公司列
    driver.get(get_url())
    driver.find_element(By.XPATH, '//input[@id="postid"]').send_keys(key)
    driver.find_element(By.XPATH, '//a[@class="btn-default btn-query"]').click()
    time.sleep(1)
    res = driver.page_source
    r = etree.HTML(res)
    ul_list = r.xpath('//ul[@id="companyCount"]/li')
    for li in ul_list:
        li_d = li.xpath('./a/text()')
        if '圆通' in li_d[0]:
            kd_write(li_d[0], key)
        if '申通' in li_d[0]:
            kd_write(li_d[0], key)
        if '韵达' in li_d[0]:
            kd_write(li_d[0], key)
    driver.quit()


if __name__ == '__main__':
    keys = input("输入需要查询的地区")
    driver = webdriver.Edge()
    kd100(keys)
    print('爬取完成')
