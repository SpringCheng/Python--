"""
九九乘法表

 -*- coding: UTF-8 -*-
@date: 2019/9/2 22:26 
@name: 99乘法表.py
@author：Spring
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
