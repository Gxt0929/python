# -*- coding: utf-8 -*-
import requests
import re
import os

def wangzhe():
    lol_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    r = requests.get(url, headers=headers).json()
    for i in r:
        cname = i['cname']
        ename = i['ename']

        for n in range(1, 10):
            hero_url = lol_url.format(ename, ename, n)
            img = requests.get(hero_url)
            if img.status_code == 200:
                with open(f'王者荣耀/{cname}-{n}.jpg', 'wb') as f:
                    f.write(img.content)
                    print(img.text)


if __name__ == '__main__':
    if not os.path.exists('王者荣耀'):
        os.mkdir('王者荣耀')
    wangzhe()