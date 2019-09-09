"""
自定义异常

 -*- coding: UTF-8 -*-
@date: 2019/9/8 8:42 
@name: 异常.py
@author：Spring
"""


# 自定义异常类
class MyError(Exception):
    pass


def add(a, b):
    if a < 0 or b < 0:
        raise MyError('两个参数中不能有负数')
    r = a + b
    return r


print(add(100, -100))
