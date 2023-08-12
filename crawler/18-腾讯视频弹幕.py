# -*- coding: utf-8 -*-
import requests
import re


def get_movie_name(ur):
    url = f'{ur}'
    r = requests.get(url).text
    # print(r)
    name = re.findall('lang="zh-CN"><head><title>(.*?)</title>', r)
    return name[0]


def get_movie(ur):
    url = f'{ur}'
    r = requests.get(url).text
    # print(r)
    ans = re.findall('/(.*?).html"><meta itemprop="name"', r)
    return ans[0][-11::]


def txsp(i, j, movie):
    url = f'https://dm.video.qq.com/barrage/segment/{movie}/t/v1/{i}/{j}'

    r = requests.get(url).json()
    # print(r)
    maxx = len(r['barrage_list'])

    for n in range(maxx):
        print(r['barrage_list'][n]['content'])
        try:
            f.write(f"{r['barrage_list'][n]['content']}\n")
        except UnicodeEncodeError:
            continue


if __name__ == '__main__':
    ur = input('输入电影地址)')
    movie = get_movie(ur)
    j = 30000
    i = 0
    with open(f'{get_movie_name(ur)}.csv', 'w') as f:
        while 1:
            try:
                strr = txsp(i, j, movie)
                f.write(f'{strr}\n')
                i = j
                j = j + 30000
            except Exception:
                break
