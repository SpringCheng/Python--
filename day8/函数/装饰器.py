"""

@date: 2019/9/10 9:53 
@author：Spring
"""


def add(a, b):
    r = a + b
    return r


def mul(a, b):
    r = a * b
    return r


def new_add(a, b):
    r = add(a, b)
    m=mul(a,b)
    return r,m


# 希望函数在计算前打印开始计算，计算结束后打印计算完毕
print(new_add(123, 345))
