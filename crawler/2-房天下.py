import requests
import re
from lxml import etree

def fangtx(page):
    url = f'https://gy.newhouse.fang.com/house/s/b{page}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    resp = response.text
    # print(resp)

    res = etree.HTML(resp)
    li_list = res.xpath('.//div[@id="newhouse_loupan_list"]/ul/li')

    with open(f'fangtx{page}.csv', 'w') as f:
        for li in li_list:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()')
            for na in name:
                final_name = na.strip()
            size = li.xpath('.//div[contains(@class, "house_type clearfix")]//text()')
            b = ''
            for si in size:
                b += si.strip()
                size = b
            dz = li.xpath('.//div[contains(@class, "address")]/a/@title')
            price = li.xpath('.//div[@class="nhouse_price"]')[0].xpath('string(.)').strip()
            tel =li.xpath('.//div[@class="tel"]')[0].xpath('string(.)').strip()
            f.write(f'{final_name}, {size}, {dz}, {price}, {tel}\n')
if __name__ == '__main__':
    for i in range(91, 99):
        fangtx(i)