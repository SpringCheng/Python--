"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 15:08 
@author：Spring
"""


class Dog:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def names(self):
        print('%s在叫' % (self.name))

    def ages(self):
        print('狗的年龄是%d' % (self.age))

    def genders(self):
        print('狗的性别是%s' % (self.gender))

    def heights(self):
        print('狗的身高是%d' % (self.height))


d1 = Dog('旺财', 1, '男', 30)
d1.names()
d1.ages()
d1.genders()
d1.heights()
