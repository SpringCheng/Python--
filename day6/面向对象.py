"""


 -*- coding: UTF-8 -*-
@date: 2019/9/5 1:55 
@name: 面向对象.py
@author：Spring
"""

"""


class Change():
    var1 = 100
    var2 = 200
    def f1():
        print('这是class中的方法')


Change.var1 = 300
print(Change.var1)
print(Change.var2)
print(Change.f1())


class Pdd():
    var1=100
    var2=200

    def func1(self):
        print('这是类的内部函数1')
    @classmethod          #使用@classmethod使得方法变成类方法，
    def func2(cls):
        print('这是类的内部函数2')
        print(cls.var1)
print(Pdd.func2())
print(Pdd.func1())
"""


class AA():
    def __init__(self, var1):
        self.name = var1
        print('我是父类的初始化函数')

    def func1(self):
        print('我是' + self.name + '!')

    def func2(self):
        print('我是父类的第三个方法')


class BB(AA):
    print('我是子类')

    def __init__(self, var1):
        self.name = var1
        print('我是子类重写父类的初始化函数方法' + self.name)

    def func1(self):
        print('我是子类重写父类的方法')


a1 = BB('cheng')
a1.func1()
a1.func2()

