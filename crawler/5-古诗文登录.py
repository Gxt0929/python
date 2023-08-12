# -*- coding: utf-8 -*-
import requests
import re
from chaojiying import Chaojiying_Client

session = requests.Session()
# 获取__VIEWSTATE
def get_gushiwen():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    r = session.get(url).text
    vie = re.search('id="__VIEWSTATE" value="(.*?)"', r).group(1)
    return vie

# 识别验证码
def code():
    url = 'https://so.gushiwen.cn/RandCode.ashx'
    r = session.get(url).content
    with open('code.jpg', 'wb') as f:
        f.write(r)
    chaojiying = Chaojiying_Client('160837538', 'guo22917', '948104')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    code = chaojiying.PostPic(im, 1004)['pic_str']
    return code

def gushiwen():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    data = {
    "__VIEWSTATE": f'{get_gushiwen()}',
    "__VIEWSTATEGENERATOR": "C93BE1AE",
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "13339681690",
    "pwd": "guo22917",
    "code": f"{code()}",
    "denglu": "登录"
}
    r = session.post(url, headers=headers, data=data).text
    with open('gushiwen.html', 'w', encoding='utf-8') as f:
        f.write(r)


if __name__ == '__main__':
    gushiwen()
