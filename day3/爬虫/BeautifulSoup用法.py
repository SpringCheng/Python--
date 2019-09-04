"""


 -*- coding: UTF-8 -*-
@date: 2019/8/31 17:28 
@name: BeautifulSoup用法.py
@author：Spring
"""

import requests
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
# 把网页解析为beautifulsoup对象
soup = BeautifulSoup(html, 'html.parser')
# item = soup.find('div')  # 提取首个div元素内容
items = soup.find_all(class_='books')
for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    brief = item.find(class_='info')
    # print('想找的数据在这里：\n', item)
    print(kind.text, '\n', title.text, title['href'], '\n', brief.text, '\n')
print(type(kind), type(title), type(brief))
# print(items)
# print(type(item))  # 打印的数据类型为<class 'bs4.element.ResultSet'>，看成是list
