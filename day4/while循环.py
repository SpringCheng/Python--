"""
猜数字大小

 -*- coding: UTF-8 -*-
@date: 2019/9/2 22:19 
@name: while循环.py
@author：Spring
"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入数字：'))
    if number < answer:
        print("猜小了")
    elif number > answer:
        print("猜大了")
    else:
        print('恭喜你答对了！')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商有点低')
