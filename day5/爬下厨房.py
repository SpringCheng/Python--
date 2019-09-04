"""


 -*- coding: UTF-8 -*-
@date: 2019/9/3 12:37 
@name: 爬下厨房.py
@author：Spring
"""

import requests
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# 找到所有class为info pure-u的div标签
list_foods = bs_foods.find_all('div', class_='info pure-u')

# 创建空列表
list_all=[]
# 提取数据
# 找到列表中第一个元素的a标签
tag_a = list_foods[0].find('a')
# 提取a标签的文本内容
name = tag_a.text[17:-13]
# 提取URL地址
URL = 'http://www.xiachufang.com' + tag_a['href']
print(name)
print(URL)
# 提取
tag_p = list_foods[0].find('p', class_='ing ellipsis')
ingredients = tag_p.text[0:-1]
print(tag_p)
print(ingredients)

