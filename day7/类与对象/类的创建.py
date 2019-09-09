"""

 -*- coding: UTF-8 -*-
@date: 2019/9/8 13:56 
@author：Spring
"""


class MyClass():
    pass


print(MyClass)
mc=MyClass()
print(mc,type(mc))
# isinstance()检查一个对象是一个类的实例
result=isinstance(mc,MyClass)
print(result)
