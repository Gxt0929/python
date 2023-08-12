# -*- coding: utf-8 -*-

import requests


def buff():
    url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=1&category_group=rifle&exterior=wearcategory0&use_suggestion=0&_=1684248169514'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
        'cookie': '_ntes_nuid=7a20a834db8a859465f0eb185ba7151e; _ntes_nnid=7a20a834db8a859465f0eb185ba7151e,1657629788350; _ga=GA1.2.69387636.1660019615; nts_mail_user=gxt22917@163.com:-1:1; __bid_n=18510c200c59c781e84207; FEID=v10-dbb6b1148d9c48722e05bc3af22a76bca7b7cab9; __xaf_fpstarttimer__=1671023427918; __xaf_thstime__=1671023428284; FPTOKEN=P4AySasZeuFh9NI6yG9/bQyK6cSxiX7u+wT2m6fPLJQdYP1bQbG83etPOMj7qtZdSGfmMhanYTHTWzvDIdWHZk/cxkUoYmWZyRQq6AuQY86C4iBwnWaqaUff34RGcXN3riMeQNA2O+nCkGyslqq8SxWfS42ER2qwWz4aIFiNFpKuhvbqV1xID9D+SQBunOmxwp4ks0bhODO3tPwA8TobVfVHj+Ix50UB+dgqfEf9zL70iyGeDVouFQuEeAyrtyUmEKwY8bEJa9j+mqQbMU/Uz4XMXfFhViJiLjnZx0urAv7o4f0PwG4NXuROYHop2eNygQ5qygE/tlpX1iiyjbamOgeqfYQUp6M5PHn2ZPX5lN3KtM/yaHY/jtA96GujfBPZGdSo0iqjdIFnnWn3Y1XlLQ==|rek5gpJk/Yv3SpNyvx+xkNc8hZ4lMiXi0ljSDO5c4WI=|10|cb4d982de343ca11407791f5a2ff9ff0; __xaf_fptokentimer__=1671023428547; NTES_P_UTID=08HpThpgQgpc49ubvairhMM2x7m2ZCDS|1674286079; Device-Id=aPaNlA63catceCq4kFir; Locale-Supported=zh-Hans; game=csgo; NTES_YD_SESS=bP1DgvrzGKko8mckIepkjHuaDQ1AEeLZWgp_h8PxII7miAPuiaN2.He1A.sl0GqAnGxsnWBvFNp4_MJqkw0DPKQf8PkJrQHj2i.2_Cucr8LTXM0nXWsbWKcW0vFWrlOgCnJ0uuyLKv9.TAG4aikvL9caGHZ53IO71i8FYQZ_Xfa16Lj8fW0hiuQ3wkGQB98NabpLEDttPBH00rLXKGIVhMEMbn9Mv3xHckS34c5emRdfd; S_INFO=1684248073|0|0&60##|13339681690; P_INFO=13339681690|1684248073|1|netease_buff|00&99|null&null&null#guz&520100#10#0|&0||13339681690; session=1-TPg9q6599rzLm5MiFbTiE2kBtQAgWahsPmXep_Zjei5G2038400502; csrf_token=IjdiZjM4MGYwODBhOWIwYjhmNWI3OTgwOGYwMmNiODRkNTcyZjJiMGQi.F0Un6g.All_UR67LG_-W0Kh066Q-fdSGsg',
        'referer': 'https://buff.163.com/market/csgo'
    }
    r = requests.get(url, headers=headers).json()
    res_list = r['data']['items']
    for res in res_list:
        print(res)


if __name__ == '__main__':
    buff()