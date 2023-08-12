# -*- coding: utf-8 -*-
import requests
import re

url = 'https://v.qq.com/x/cover/mzc002006z017c8/z0046w40cr8.html'
r = requests.get(url).text
# print(r)
ans = re.findall('/(.*?).html"><meta itemprop="name"', r)
name = re.findall('lang="zh-CN"><head><title>(.*?)</title>', r)
print(name[0])
# print(ans[0][-11::])