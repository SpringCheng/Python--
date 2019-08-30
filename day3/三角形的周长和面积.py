"""
判断输入的边长能否构成三角形
如果能就计算出三角形的周长和面积

 -*- coding: UTF-8 -*-
@date: 2019/8/30 22:03 
@name: 三角形的周长和面积.py
@author：Spring
"""

import math

a = int(input('请输入三角形的第一条边:'))
b = int(input('请输入三角形的第二条边:'))
c = int(input('请输入三角形的第三条边:'))
if a + b > c and a + c > b and b + c > a:
    print('周长:%f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积:%f' % area)
else:
    print('不能构成三角形')
