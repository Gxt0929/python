# -*- coding: utf-8 -*-

import requests
import re


def esc(page, f):
    url = f'https://mapi.guazi.com/car-source/carList/pcList?versionId=0.0.0.0&page={page}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
    }
    params = {
    "versionId": "0.0.0.0",
    "sourceFrom": "wap",
    "deviceId": "20d35b0a-ee65-45df-b63a-e427449d8338",
    "osv": "Windows 10",
    "tag": "-1",
    "priceRange": "0,-1",
    "tag_types": "10010",
    "page": "1",
    "pageSize": "20",
    "city_filter": "12",
    "city": "12",
    "guazi_city": "12",
    "qpres": "673110489110921216",
    "platfromSource": "wap"
    }
    r = requests.get(url, params=params, headers=headers).json()
    postList = r['data']['postList']
    for carlist in postList:
        # 字段: 款式,总功率, 续航里程, 电池容量, 颜色,二手价格,新车价格
        # print(carlist)
        title = carlist['title']
        clue_id = carlist['clue_id']
        price = carlist['price'].replace('&#57808;', '7').replace('&#58149;', '4').replace('&#58397;', '1').replace('&#58585;', '').replace('&#58670;', '9').replace('&#58928;', '2').replace('&#59246;', '8').replace('&#59537;', '5').replace('&#59854;', '0').replace('&#60146;', '3').replace('&#60492;', '6').replace('&#63426;', '').replace('&#63626;', '7')
        first_price = carlist['first_pay'].replace('&#57808;', '7').replace('&#58149;', '4').replace('&#58397;', '1').replace('&#58585;', '').replace('&#58670;', '9').replace('&#58928;', '2').replace('&#59246;', '8').replace('&#59537;', '5').replace('&#59854;', '0').replace('&#60146;', '3').replace('&#60492;', '6').replace('&#63426;', '').replace('&#63626;', '7')
        car_url = f'https://www.guazi.com/Detail?clueId={clue_id}'
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
            'cookie': 'uuid=20d35b0a-ee65-45df-b63a-e427449d8338; sessionid=23659fe6-8a5e-4517-c0af-30ff619a9155; cainfo=%7B%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%2220d35b0a-ee65-45df-b63a-e427449d8338%22%7D',
            'referer': 'https://www.guazi.com/buy'
        }
        car_r = requests.get(car_url, headers=header).content.decode()
        power_val = re.findall('总功率";a(.*?).value="(.*?)"', car_r)[0][1]
        con_val = re.findall('"续航里程";a(.*?).value="(.*?)"', car_r)[0][1]
        dc_val = re.findall('电池容量";a(.*?).value="(.*?)"', car_r)[0][1]
        temp = re.sub('[\u4e00-\u9fa5]', '', dc_val)
        color_val = re.findall('"车身颜色";a(.*?).value="(.*?)"', car_r)[0][1]
        newRmb_val = re.findall('"新车含税价";a(.*?).value="(.*?)"', car_r)[0][1]
        pri = price + '+' + first_price + '(首付)'
        print(title)
        f.write(f'{title},{power_val},{con_val},{temp},{color_val},{pri},{newRmb_val}\n')


def main():
    for i in range(1, 81):
        esc(i, f)


if __name__ == '__main__':
    with open(f'新能源.csv', 'w') as f:
        f.write(f'{"款式"},{"总功率"},{"续航里程"},{"电池容量(空白代表暂无数据)"},{"颜色"},{"二手价格"},{"新车价格"}\n')
        main()


