"""

@date: 2019/9/11 22:53 
@author：Spring
"""
import random

for i in range(5):
    # sample() 随机输出N个元素，返回列表
    # 第一个参数为列表，第二个参数为输出的个数
    user_email = ''.join(random.sample('12309876709534467523sdsaasdfasdfty56', 8))+"@163.com"
    print(user_email)
