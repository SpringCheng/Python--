"""


 -*- coding: UTF-8 -*-
@date: 2019/9/5 0:44 
@name: demo.py
@author：Spring
"""

# d={'name':'jason','dob':'2000-01-01','gender':'male'}
# list_1=[]
# for k in d:
#     list_1.append(k)
# print(list_1)

l = [1, 2, 3, 4, 5, 6]
for k in range(0, len(l)):
    if k < 5:
        print(l[k])
l = [1, 2, 3, 4, 5, 6, 7]
for index,item in enumerate(l):
    if index<5:
        print(item)
