# -*- coding: utf-8 -*-
import datetime
import requests
import re
import time

def openreadtxt(file_name):
    data = []
    file = open("补益类用药.txt", 'r', encoding='utf-8')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        tmp_list = row.split(' ')  # 按‘，’切分每行的数据
        # tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
        tmp_list = re.sub(u"([^\u0030-\u0039])", "", tmp_list[0])
        data.append(tmp_list)  # 将每行数据插入data中
    return data
#
# def fung():
#     url = 'https://api.m.jd.com/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
#         'Cookie': '__jdv=125919621|direct|-|none|-|1690514869894; __jda=125919621.1690514869893932221073.1690514870.1690569204.1690605894.3; __jdc=125919621; shshshfpb=ehmZh5TCL08c_iISk3nbktg; wlfstk_smdl=g6flfchdqxaw03pf2btmep8p6kxz19mh; __jdb=125919621.23.1690514869893932221073|3.1690605894',
#         'Referer': 'https://item.yiyaojd.com/'
#     }
#     t = int(time.time() * 1000)
#     timestamp = t / 1000.0  # 将时间戳除以1000，转换为秒
#     dt = datetime.datetime.fromtimestamp(timestamp)
#     formatted_date = dt.strftime('%Y%m%d%H%M%S%f')[:-3]  # 格式化日期字符串，去掉最后三位微秒数
#     params = {
#     "appid": "pc-item-soa",
#     "functionId": "pc_detailpage_wareBusiness",
#     "client": "pc",
#     "clientVersion": "1.0.0",
#     "t": f"{int(time.time()*1000)}",
#     "body": "{\"skuId\":3156378,\"cat\":\"13314,21909,21923\",\"area\":\"24_2144_3909_58335\",\"shopId\":\"1000015441\",\"venderId\":1000015441,\"paramJson\":\"{\\\"platform2\\\":\\\"100000000001\\\",\\\"specialAttrStr\\\":\\\"p0ppppppppp2ppppppppppp1ppp\\\",\\\"skuMarkStr\\\":\\\"00\\\"}\",\"num\":1,\"bbTraffic\":\"\"}",
#     "h5st": f"{formatted_date};gg956nmt33gi3zh6;fb5df;tk03w76541b5118nkwAE27V05rivYRkt2LFqMOPJKBBiQ6z9Id06mkF0FFXV5X96dPsbzKmCOa44nh9YhFekocj7SxUV;3e4e6b4dd66e72c59f832d2efe62633b;4.1;{int(time.time() * 1000)};ee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a3980acde1a10effcc27fd84ad69b6a255fa2bacbfc5a0cc8222e4ac53b669906820b1461c75971601a3f031b5c1f40b721502f3b79e32d29b726ebec75a213493a818f67211b187fcf51e032e0b772bee8c70e4a1d7502aa775b148a504a31d627ad8178a35e9040232318a8b13829c3d61cc896d07e561834b5a1106c4f6e2096b6239320011f5233377fa703bb7da4d6f05a2f6c81ea17f9abd5459ee88109ae9929ef3582c3e76d82a10581aa3aa6d43aad213b7dfc2506600891f8c9baf64c",
#     "x-api-eid-token": "jdd03YFITMDSKEM5TVG4JOVTMLF3W2MZMLX5YWE2T6K32DXKGCUWYRWCZHQSXVMISSDR5UJHJLL55D2E5HXXQNPO34R3DGAAAAAMJUAMKVMAAAAAACISSWUQE7A472QX",
#     "loginType": "3",
#     "uuid": "125919621.1690514869893932221073.1690514870.1690569204.1690605894.3"
#     }
#     r = requests.get(url, headers=headers, params=params)
#     print(r)

def fun_c(sku, f):
    # urls = f'https://item.yiyaojd.com/{sku}.html'
    # headerss = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    #     'Cookie': 'shshshfp=cd89878c9379105da4896e5e30da91ca; shshshfpa=fd6f18bb-d36c-8638-3368-5df61bb456e5-1669435613; 3AB9D23F7A4B3C9B=XRKYMMUZAG3FD2WUNG3VLHZJT56FOPEFH7XLTEME5OQHFA3RMEWLUL4A5HXTDFRPMMDHZAKGDL3RAZ7GWAXLB55X4A; __jdu=1690514869893932221073; shshshfpx=fd6f18bb-d36c-8638-3368-5df61bb456e5-1669435613; PCSYCityID=CN_520000_520400_0; mba_muid=1690514869893932221073; __jd_ref_cls=LoginDisposition_Go; shshshfpb=k9eYhE5_oQU478O6_kgIYQA; x-rp-evtoken=N-nAb5Oj6OS1u8hkvixIgNpO9gMkukqKii_kF7MYFSS_hXHiycsyZpNvEMEtSf3pHqFJ8wOpvcJOO-hXZpNm1H_n_FenzQ0Gqwwt8asPdkjP3pxnPB8BzSG7Fjff_vIhmfXdtJHu3t6UFujlNnT2niV5HstIA1JpCNsCzvOQjyMc8VliWCT5_7yJy__OMkL8HLxGgtODZxSujeqzaICc7--F04SPNAvu0m41e8gjUQs%3D; jsavif=0; jsavif=0; areaId=24; __jdc=122270672; unpl=JF8EAKpnNSttX05QVhMDSRsXGwhXW11aHkRWOzcAAV4LQgNXTAUTFxl7XlVdXxRKER9tZhRVXVNIVg4ZBisSEXtdVV9fDE4TAGtnNWRtW0tkBCsCHBoRT11RV1oAQh8BZ2UGV15YSlIHKwMrEhhPbVdYVABKFQZuYA1XbWhOVAQaAB4WGEhaZF9tCXtWbWlhA1RVWgZUAhMDHxIVQlpcV1UKQxUAbGQFVVtae1U1GA; __jda=122270672.1690514869893932221073.1690514870.1690646310.1690651415.7; ipLoc-djd=24-2189-2194-8692; token=210d8b84f52bc53bf029d7e6a3582020,2,939250; __tk=SjB3ZkpSSEzlicyCkzkIZl5FTNVYklbVTyCYpDzkoUPmlzf4SlVPZc5Fk1zlklkajz3JqbRd,2,939250; 3AB9D23F7A4B3CSS=jdd03XRKYMMUZAG3FD2WUNG3VLHZJT56FOPEFH7XLTEME5OQHFA3RMEWLUL4A5HXTDFRPMMDHZAKGDL3RAZ7GWAXLB55X4AAAAAMJUKZMB5QAAAAACUX766XZOVEEHAX; _gia_d=1; __jdb=122270672.3.1690514869893932221073|7.1690651415; __jdv=122270672|www.xiaoxiaodediyi.xyz|t_1003545251_|tuiguang|645b90c86ad241cdbdea4d2b8fcf6948|1690651769730',
    #     'Referer': 'https://union-click.jd.com/'
    # }
    # res = requests.get(urls, headers=headerss).text
    # med_name = re.findall('<title>(.*?)【行情 报价 价格 评测】', res)[0]
    # med_imgs = re.findall('data-origin="(.*?)" alt="', res)[0]
    # med_type = re.findall('<dt>药品分类</dt><dd>(.*?)</dd>', res)[0]
    # med_brand = re.findall("<li title='(.*?)'>品牌：", res)[0]
    # i = 0

    for i in range(0, 11):
        url = f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t={int(time.time() * 1000)}&loginType=3&uuid=125919621.1690514869893932221073.1690514870.1690514870.1690514870.1&productId={sku}&score=0&sortType=5&page={i}&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
            'Cookie':'; __jdc=125919621; __jdv=125919621|direct|-|none|-|1690514869894; __jdb=125919621.4.1690514869893932221073|1.1690514870',
            'Referer':'https://item.yiyaojd.com/'
            }
        r = requests.get(url, headers=headers).json()
        for comm in r["comments"]:
            print(comm)
            try:
                content = comm["content"].replace(',', '，').replace('\n', ' ')
                creationTime = comm["creationTime"].replace(',', '，')
                imgs = ''
                for img in comm['images']:
                    imgs += img['imgUrl'] + ';'

                location = comm["location"].replace(',', '，')
                nickname = comm["nickname"].replace(',', '，')
                score = comm["score"]
                usefulVoteCount = comm["usefulVoteCount"]
                plusAvailable = comm["plusAvailable"]
                if plusAvailable != 201:
                    plusAvailable = '普通用户'
                else:
                    plusAvailable = 'PLUS会员'
                referenceName = comm["referenceName"].replace(',', '，')
                referenceId = comm["referenceId"]
            except KeyError:
                pass
            f.write(f'{nickname},{plusAvailable},{content},{imgs},{score},{referenceName},{referenceId},{creationTime},{location},{usefulVoteCount}\n')

if __name__ == '__main__':
    with open('finalls.csv', 'w') as f:
        f.write(f'{"用户名称"},{"会员级别"},{"评论内容"},{"评论图片链接"},{"用户评分"},{"商品标题"},{"商品sku"},{"评论时间"},{"用户所在城市"},{"点赞数"}\n')
        data = openreadtxt('test.txt')
        for sku in data:
            # print(sku)
            fun_c(sku, f)
