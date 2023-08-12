# -*- coding: utf-8 -*-
import requests
import re
import os
from pyquery import PyQuery as pq
from lxml import etree

def jianli(i):
    url = f'https://sc.chinaz.com/jianli/free_{i}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    response = requests.get(url, headers=headers).text

    ret = etree.HTML(response)
    j = 0
    ret = pq(response)
    div_list = ret('img')
    # print(div_list)
    for div in div_list[1:]:
        with open(f'jianli{i}-{j}.jpg', 'wb') as f:
            im = pq(div).attr('src')
            imm = 'https:'+ im
            img = requests.get(imm).content
            f.write(img)
            print('保存成功')
            j += 1


if __name__ == '__main__':
    for i in range(2, 921):
        jianli(i)
