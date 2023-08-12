# -*- coding: utf-8 -*-
import requests
import re
import os


def baidu(word, page):
    url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8995231969422190563&ipn=rj&ct=201326592&is=&fp=result&fr=&word={word}&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={page*30}&rn=30&gsm=3c&1683376627392='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }
    r = requests.get(url, headers=headers).text
    res = re.findall('"hoverURL":"(.*?)",', r)
    i = 1
    for img in res:
        imgs = requests.get(img).content
        with open(f'{word}/{page}-{i}.jpg', 'wb') as f:
            f.write(imgs)
            print(imgs)
            i += 1


if __name__ == '__main__':
    word = input()
    if not os.path.exists(word):
        os.mkdir(word)
    for page in range(1, 11):
        baidu(word, page)


