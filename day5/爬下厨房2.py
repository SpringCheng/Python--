"""


 -*- coding: UTF-8 -*-
@date: 2019/9/3 15:45 
@name: 爬下厨房2.py
@author：Spring
"""

import requests
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# 查找最小的父级标签
list_foods = bs_foods.find_all('div', class_='info pure-u')

# 创建一个空列表，用来存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('a')
    # 获取菜名
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com' + tag_a['href']
    # 提取第0个父级标签中的p标签
    tag_p = food.find('p', class_='ing ellipsis')
    # 获取食材
    ingredients = tag_p.text[1:-1]
    # 将菜名，URL，食材，封装为列表，添加进list_all
    list_all.append([name, URL, ingredients])
# print(list_all,end='\n')
for i in list_all:
    with open('list_foods.txt','a',encoding='utf-8') as lf:
        lf.write(str(i)+'\n')
        lf.close()
