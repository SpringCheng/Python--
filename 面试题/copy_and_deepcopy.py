"""


 -*- coding: UTF-8 -*-
@date: 2019/9/4 7:39 
@name: copy_and_deepcopy.py
@author：Spring
"""

import copy

a = ('a', 'b', 'c')
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
if c == d:
    print("c和d的值相等")
if id(c) == id(d):
    print("c和d的地址相等")

print(b)
print(c)
print(d)
print(id(b))
print(id(c))
print(id(d))
