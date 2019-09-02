"""


 -*- coding: UTF-8 -*-
@date: 2019/8/31 15:59 
@name: response.text用法.py
@author：Spring
"""

import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men4.0.html')
res.encoding='utf-8'
novel = res.text
print(novel[:100])
k = open('获取网页.txt', 'a+')
k.write(novel)
k.close()
