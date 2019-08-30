"""
练习if语句的使用

 -*- coding: UTF-8 -*-
@date: 2019/8/30 21:41 
@name: 掷骰子.py
@author：Spring
"""

import random

value = random.randint(1, 6)

if value == 1:
    result = '唱歌'
elif value == 2:
    result = '跳舞'
elif value == 3:
    result = '跑步'
elif value == 4:
    result = '看电影'
elif value == 5:
    result = '玩游戏'
else:
    result = '睡觉'
print(result)


