"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 16:41 
@author：Spring
"""


class Animal:
    def run(self):
        print('动物会跑')

    def sleep(self):
        print('动物睡觉')

    def bark(self):
        print('动物嚎叫')


class Dog(Animal):
    def run(self):
        print('狗跑的很快')


d = Dog()
d.run()
