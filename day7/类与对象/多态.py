"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 18:27 
@author：Spring
"""


class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


a = A('孙悟空')
b = B('猪八戒')


# 定义一个函数
def say_hello(obj):
    print('你好呀%s' % obj.name)


def say_hello2(obj):
    # 做类型检查
    if isinstance(obj, A):
        print('你好%s' % obj.name)


# 对于say_hello这个函数来说，只要对象中含有name属性，它就可以作为参数传递，
# 这个函数并不会考虑对象的类型，只要有name即可
say_hello2(a)

# 在say_hello2()中做了类型检查，只有obj是A类型的对象时，才可以正常使用，其他类型的对象都无法使用该函数，这个函数违反了多态
# 违反了多态的函数，只适用于一种函数函数，无法处理其他类型的对象，这样导致函数的适用性非常的差
say_hello2(b)

