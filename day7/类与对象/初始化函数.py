"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 14:42 
@author：Spring
"""


class Person():
    def say_name(self):
        print('大家好我是%s' % self.name1)
        print('大家好我是%s' % self.name2)
        print('大家好我是%s' % self.name3)

    def __init__(self, a, b, c):
        self.name1 = a
        self.name2 = b
        self.name3 = c
        print('我是初始化函数')


p2 = Person('ts', 'zbj', 'shs')
p2.say_name()
