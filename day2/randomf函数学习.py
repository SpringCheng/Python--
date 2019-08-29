"""
random函数的练习

 -*- coding: UTF-8 -*-
@date: 2019/8/30 3:54 
@name: randomf复习.py
@author：Spring
"""

import random

a = random.random()  # 随机从0-1之间抽取一个数
print(a)

b=random.randint(0,100) #随机从0-100之间抽取一个数
print(b)

c=random.choice('abcdefg') #随机从字符串、列表、字典等对象中抽取一个元素（可能会重复）
print(c)

d=random.sample('abcdefg',3) #随机从字符串、列表、字典等对象中抽取n个不重复的元素，返回一个列表
print(d)

items=[1,2,3,4,5,6]

random.shuffle(items) # 随机洗牌，比如打乱顺序
print(items)
