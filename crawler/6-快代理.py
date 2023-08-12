# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree
import time

# 检查ip是否可用
def check(ips):
    url = 'http://httpbin.org/ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }
    proxies = {
        'http': ips
    }

    r = requests.get(url, proxies=proxies, headers=headers)
    if r.status_code == 200:
        return 1
    else:
        return -1



# 获取代理ip
def daili(page):

    url = f'https://www.kuaidaili.com/free/inha/{page}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }
    r = requests.get(url, headers=headers).text
    rs = etree.HTML(r)
    ip_list = rs.xpath('//*[@id="list"]/table/tbody/tr')
    proxie = []
    for ip in ip_list:
        s = ip.xpath('.//td/text()')
        ips = f"{s[0] +':'+ s[1]}"
        if check(ips):
            proxie.append(ips)
            print(ips)



if __name__ == '__main__':
    for i in range(1, 11):
        daili(i)
        time.sleep(2)
