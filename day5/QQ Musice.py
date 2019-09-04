"""


 -*- coding: UTF-8 -*-
@date: 2019/9/3 17:22 
@name: QQ Musice.py
@author：Spring
"""
from bs4 import BeautifulSoup
import requests

res_music=requests.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6\
')
bs_music=BeautifulSoup(res_music.text,'html.parser')
list_music=bs_music.find_all('a',class_='js_song')
for music in list_music:
    print(list_music)
