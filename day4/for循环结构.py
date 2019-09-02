"""
range(101)  =0~100
range(1,10) =1~99
range(1,100,2) =1~99的奇数序列  因此可以求范围内的奇数或偶数的和range(2,101,2)


 -*- coding: UTF-8 -*-
@date: 2019/9/2 22:07 
@name: for循环结构.py
@author：Spring
"""
# 1~100求和
sum = 0
for i in range(101):  # 等于(0,101)  不包括最后一位
    sum += i
print(sum)

# 1~100 求奇数和

sum1 = 0
for i in range(1, 101, 2):
    sum1 += i
print(sum1)

# 1~100 求偶数和方法一
sum2 = 0
for i in range(2, 101, 2):
    sum2 += i
print(sum2)

# 1~100偶数求和方法二
sum3 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum3 += i
print(sum3)
