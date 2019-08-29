"""


 -*- coding: UTF-8 -*-
@date: 2019/8/30 4:14 
@name: csv模块.py
@author：Spring
"""
# 读取CSV文件的内容，reader()函数是键CSV文件每一行作为一个字符串列表返回
import csv

with open(r'C:\Users\Mloong\Desktop\aaa\aaa.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 写入到CSV文件
with open(r'C:\Users\Mloong\Desktop\aaa\aaa.csv', 'a', encoding='utf-8') as F:
    Writer = csv.writer(F)   
    Writer.writerow([1, 2, 3, 4, 5, 6])
