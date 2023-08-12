# -*- coding: utf-8 -*-
import requests
import time

def bili():
    url = 'https://api.live.bilibili.com/msg/send'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
        "cookie": "buvid3=4540C300-9E15-B95F-17C3-05B28CA55DA625852infoc; _uuid=7C454810F-6B2F-E1D1-61044-3D9A22996B10A24752infoc; buvid4=8F481572-EB7E-1CDF-04BB-32208F7C4A6D26597-022071419-5B4tQljmHlJ9ektYLa3uhQ%3D%3D; i-wanna-go-back=-1; nostalgia_conf=-1; is-2022-channel=1; buvid_fp_plain=undefined; fingerprint3=1601c9fb5bf7af8b543f5ee08051eaac; LIVE_BUVID=AUTO7416595407281318; hit-dyn-v2=1; b_nut=100; rpdid=|(m~RumummR0J'uYY)YmYlmJ; header_theme_version=CLOSE; blackside_state=0; CURRENT_BLACKGAP=0; CURRENT_PID=0098ab30-ce0f-11ed-8e36-1fd0449e419a; CURRENT_FNVAL=4048; CURRENT_QUALITY=120; fingerprint=3f74420ce50a32240f9792efb26dd181; buvid_fp=3f74420ce50a32240f9792efb26dd181; FEED_LIVE_VERSION=V8; home_feed_column=5; b_ut=7; browser_resolution=1865-961; SESSDATA=79dd8c6f%2C1699448509%2C5e5e3%2A52; bili_jct=3e7a4df6a8aca45a383734258e6474fd; DedeUserID=473914872; DedeUserID__ckMd5=31235188d1fc1b10; bp_video_offset_473914872=794818088161771600; _dfcaptcha=75b08504d668d9e01c8a8400dcc89933; b_lsid=813D1056B_1881326C2FE; share_source_origin=QQ; bsource=share_source_qqchat; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1681815193,1683948589; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1683948589; PVID=3"
        }

    data = {
        'bubble': '0',
        'msg': 'holo',
        'color': '16777215',
        'mode': '1',
        'fontsize': '25',
        'rnd': int(time.time()),
        'roomid': '27806431',
        'csrf': 'd03192b65b8f79a1619551848623bc73',
        'csrf_token': 'd03192b65b8f79a1619551848623bc73'
    }

    r = requests.post(url, headers=headers, data=data).text
    print(r)


if __name__ == '__main__':
    bili()
