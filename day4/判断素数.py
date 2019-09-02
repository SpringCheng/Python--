"""
输入一个整数判断是否是素数(只能被自身和1整除的数)

 -*- coding: UTF-8 -*-
@date: 2019/9/2 22:31 
@name: 判断素数.py
@author：Spring
"""

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)