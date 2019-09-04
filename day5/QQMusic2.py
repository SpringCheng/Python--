"""


 -*- coding: UTF-8 -*-
@date: 2019/9/3 18:51 
@name: QQMusic2.py
@author：Spring
"""

import requests

res_music = requests.get(
    'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=57641502012629446&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=1086886777&loginUin=867912954&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
json_music = res_music.json()
list_music=json_music['data']['song']['list']
# print(list_music)
for music in list_music:
    print(music['name'])
    print('所属专辑：'+music['album']['name']+'\n')
    print('URL:'+music['url'])
    # print('歌手：'+music['singer'])
    # print('播放时长：'+int(music['interval'])+'秒')
