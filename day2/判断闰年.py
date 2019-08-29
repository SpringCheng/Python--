"""
闰年是能被4整数且不能被100整除或者能被400整除

 -*- coding: UTF-8 -*-
@date: 2019/8/30 2:40 
@name: 判断闰年.py
@author：Spring
"""


years = int(input('请输入年份：'))
if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
    print('该年是闰年')
else:
    print('该年是平年')
