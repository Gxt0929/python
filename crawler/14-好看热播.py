# -*- coding: utf-8 -*-
from multiprocessing import Pool

import time

import requests
import re
from contextlib import closing
import os


def rebo():
    m = 1
    with open('好看热播.csv', 'w') as f:
        f.write(f'{"视频排名"},{"视频标签"},{"发布时间"},{"热播指数"},{"发布人"}\n')
        for i in range(1, 4):
            url = f'https://haokan.baidu.com/videoui/page/pc/toplist?type=hotvideo&sfrom=haokan_web_banner&pageSize=20&_format=json&page={i}'
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
            }
            r = requests.get(url, headers=headers).json()
            video_list = r['apiData']['response']['video']
            for video in video_list:
                videoName = video['title']
                videoHot = video['hot']
                videoFirstTime = video['publish_time']
                videoAuthor = video['author']
                if m <= 50:
                    f.write(f'{m},{videoName},{videoFirstTime},{videoHot},{videoAuthor}\n')
                    m += 1


def dl_viedo(i):
    mm = 1
    url = f'https://haokan.baidu.com/videoui/page/pc/toplist?type=hotvideo&sfrom=haokan_web_banner&pageSize=20&_format=json&page={i}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
    }
    r = requests.get(url, headers=headers).json()
    video_list = r['apiData']['response']['video']
    for video in video_list:
        videoName = video['title']
        videoUrl = video['videoUrl']
        videodl = requests.get(videoUrl).content
        if i == 3 and mm < 10:
            print('正在下载...')
            with open(f'{videoName}.mp4', 'wb') as g:
                g.write(videodl)
            mm += 1


if __name__ == '__main__':
    rebo()
    pool = Pool(3)
    pool.map(dl_viedo, [j for j in range(1, 4)])

    pool.close()
    pool.join()
