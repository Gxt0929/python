# -*- coding: utf-8 -*-
import json
from coll import coll_dic
import requests
import re
from lxml import etree

def coll_rank(year):
    keys, val = coll_dic(year)
    dic = dict(zip(keys, val))
    url = f'https://www.shanghairanking.cn/_nuxt/static/1683627276/rankings/bcur/{year}11/payload.js'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
        'cookie': 'Hm_lvt_af1fda4748dacbd3ee2e3a69c3496570=1683696037,1683725203,1683777521; _clck=4a2qjm|1|fbi|0; Hm_lpvt_af1fda4748dacbd3ee2e3a69c3496570=1683777571'
    }
    r = requests.get(url, headers=headers).text
    # print(r)
    nuivname = re.findall('univNameCn:"(.*?)"', r)
    prov = re.findall('province:(.*?),', r)
    scores = re.findall('score:(.*?),', r)
    classs = re.findall('univCategory:(.*?),', r)
    if year == 2015:
        bests = ''
    elif year == 2016:
        bests = ''
    elif year == 2017:
        bests = ''
    elif year == 2018:
        bests = re.findall('"28":(.*?),', r)
    elif year == 2019:
        bests = re.findall('"38":(.*?),', r)
    elif year == 2020:
        bests = re.findall('"59":(.*?),', r)
    elif year == 2021:
        bests = re.findall('"159":(.*?),', r)
    elif year == 2022:
        bests = re.findall('"271":(.*?),', r)
    elif year == 2023:
        bests = re.findall('"411":(.*?),', r)

    rankings = re.findall('ranking:(.*?),', r)

    ranking = []
    bes = []
    clas = []
    scor = []
    prove =[]
    nam = []

    with open(f'{year}.csv', 'w') as f:
        if year >= 2015 and year <= 2019:
            f.write(f'{"排名"}, {"学校名称"}, {"省市"}, {"类型"}, {"总分"}, {"生源质量"}\n')
        elif year >= 2020 and year <= 2023:
            f.write(f'{"排名"}, {"学校名称"}, {"省市"}, {"类型"}, {"总分"}, {"办学层次"}\n')

        for name in nuivname:
            if name in keys:
                nam.append(dic[name])
            else:
                nam.append(name)

        for rank in rankings:
            if rank in keys:
                ranking.append(dic[rank])
            else:
                ranking.append(rank[1:-1])

        if bests == '':
            bes.append('')
        else:
            for best in bests:
                if best in keys:
                    bes.append(dic[best])
                else:
                    bes.append(best[1:-1])

        for cla in classs:
            if cla in keys:
                clas.append(dic[cla])

        for score in scores:
            if score in keys:
                scor.append(dic[score])
            else:
                scor.append(score)

        for pro in prov:
            if pro in keys:
                prove.append(dic[pro])

        for i in range(0, len(ranking)):
            if year >= 2015 and year <= 2017:
                f.write(f'{ranking[i]},{nam[i]},{prove[i]},{clas[i]},{scor[i]},''\n')
            else:
                f.write(f'{ranking[i]},{nam[i]},{prove[i]},{clas[i]},{scor[i]},{bes[i]}\n')


if __name__ == '__main__':
     for year in range(2015, 2024):
        coll_rank(year)

