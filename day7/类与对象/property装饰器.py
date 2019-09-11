"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 16:29 
@author：Spring
"""


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter  # setter方法的装饰器：@属性名.setter
    def name(self, name):
        self._name = name


p = Person('猪八戒')
print(p.name)
p.name = '唐僧'
print(p.name)
