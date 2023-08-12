# -*- coding: utf-8 -*-

import socket
import time

import requests
from datetime import datetime, timedelta


def vpn():
    # 获取今天的日期
    today = datetime.now().date()
    tomorrow_eight_am = datetime.combine(today + timedelta(days=1), datetime.min.time()) + timedelta(hours=8)
    timestamp_tomorrow_eight_am = int(tomorrow_eight_am.timestamp())
    days_ago = 61
    date_61_days_ago = today - timedelta(days=days_ago)
    time_61_days_ago = datetime.combine(date_61_days_ago, datetime.min.time()) + timedelta(hours=8)
    timestamp_61_days_ago = int(time_61_days_ago.timestamp())

    global open
    with open('CMC.csv', 'w', encoding='utf-8') as f:
        f.write(f'{"name"},{"symbol"},{"timeclose"},{"openprice"},{"highprice"},{"lowprice"},{"close"},{"volume"},{"marketCap"}\n')
        i = 0
        while True:
            # 获取大于200w美元市值的加密货币
            try:
                url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing'
                params = {
                    "start": f"{1 + i * 100}",
                    "limit": "100",
                    "sortBy": "market_cap",
                    "sortType": "desc",
                    "convert": "USD,BTC,ETH",
                    "cryptoType": "all",
                    "tagType": "all",
                    "audited": "false",
                    "aux": "ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap",
                    "marketCapRange": "2000000~"  # 获取大于200w美元的加密货币
                }
                # 代理设置
                proxies = {
                    'https': 'http://127.0.0.1:33210',
                    'http': 'http://127.0.0.1:33211'
                }
                res = requests.get(url, params=params, proxies=proxies)
                res.raise_for_status() # 检查是否发生请求异常
                r = res.json()
                # 结束判断
                if len(r['data']['cryptoCurrencyList']) == 0:
                    break
            except requests.exceptions.RequestException as e:
                print(f"请求异常：{e}")
                time.sleep(1)
                continue
            except requests.exceptions.JSONDecodeError as e:
                print(f"JSON 解码异常：{e}")
                time.sleep(1)
                continue
            except:
                # 由于请求次数过多，被认定为攻击行为，重复请求
                time.sleep(1)

            # 处理获取到的加密货币名称和ID
            try:
                res = r['data']['cryptoCurrencyList']
            except NameError:
                print("网络连接错误，代理配置不正确，或再试一次")
                exit()
            except KeyError as e:
                print(f"解析数据时出现 KeyError 异常：{e}")
                continue
            cnt = 1
            # 获取加密货币的历史数据
            for caplist in res:
                try:
                    name = caplist['name']
                    id = caplist['id']
                    history_url = f'https://api.coinmarketcap.com/data-api/v3.1/cryptocurrency/historical'
                    params = {
                        "id": f"{id}",
                        "convertId": "2781",
                        "timeStart": f"{timestamp_61_days_ago}",
                        "timeEnd": f"{timestamp_tomorrow_eight_am}",
                        "interval": "1d"
                    }
                    response_historical = requests.get(history_url, params=params, proxies=proxies)
                    response_historical.raise_for_status()
                    resp = response_historical.json()
                    print(f'已获取{cnt}组加密货币数据----{name}')
                    cnt += 1
                except requests.exceptions.RequestException as e:
                    print(f"{name} 请求异常：{e}")  # 输出币种名称和异常信息
                    time.sleep(1)
                    continue
                except requests.exceptions.JSONDecodeError as e:
                    print(f"{name} JSON 解码异常：{e}")  # 输出币种名称和异常信息
                except:
                    # 由于请求次数过多，被认定为攻击行为，重复请求
                    time.sleep(1)

                # 对获取到的加密货币历史数据进行处理
                try:
                    response = resp['data']['quotes']
                    symbol = resp['data']['symbol']
                    for quotesList in response[32:60:]:
                        close = quotesList['quote']['close']
                        high = quotesList['quote']['high']
                        low = quotesList['quote']['low']
                        mkcap = quotesList['quote']['marketCap']
                        open = quotesList['quote']['open']
                        timeclose = quotesList['timeClose']
                        volume = quotesList['quote']['volume']
                        f.write(f'{name},{symbol},{timeclose},{open},{high},{low},{close},{volume},{mkcap}\n')
                except KeyError as e:
                    print(f"{name} 解析数据时出现 KeyError 异常：{e}")  # 输出币种名称和异常信息
                    continue
                except UnboundLocalError as e:
                    print(f"{name} 解析数据时出现 UnboundLocalError 异常：{e}")
                    continue


if __name__ == '__main__':
    socket.setdefaulttimeout(20)
    print("开始获取数据...")
    vpn()
    print("over!")
