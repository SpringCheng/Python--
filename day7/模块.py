"""


 -*- coding: UTF-8 -*-
@date: 2019/9/8 9:06
@author：Spring
"""
import modul1 as mu
from modul2 import a
import sys
print(a.var1)
print(a.test1())

# 使用“模块.变量”调用模块中的变量
print(mu.var1)
# 使用“模块.函数”调用模块中的函数
mu.mo1()
# 使用"模块.类.变量"调用模块中类的变量
print(mu.Add.var3)
# 使用"模块.类.方法"调用模块中类的方法
mu.Add.mo3()
# 使用“A=模块.类()” 创建实例
A=mu.Add()
# 实例化汇总不在需要  "模块.",
print(A.var3)
A.mo2()
print(__name__)
print(sys.platform)
