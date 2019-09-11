"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 15:37 
@author：Spring
"""


class Dog:
    def __init__(self, name):
        self.name = name

    # get_name()用来获取对象的name属性
    def get_name(self):
        return self.name

    # set_name()用来设置对象的name属性
    def set_name(self , name):
        self.name=name

    def names(self):
        print('%s在叫' % (self.name))


d1 = Dog('旺财')
d1.names()
d1.set_name('小黑')
print(d1.get_name())
