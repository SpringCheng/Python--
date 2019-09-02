"""


 -*- coding: UTF-8 -*-
@date: 2019/8/31 17:28 
@name: BeautifulSoup用法.py
@author：Spring
"""

import requests
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
print(res.status_code)
html = res.text
# 把网页解析为beautifulsoup对象
soup = BeautifulSoup(html, 'html.parser')

print(type(soup))
