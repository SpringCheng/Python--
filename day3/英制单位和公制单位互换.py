"""
英制单位英寸和公制单位厘米的互换

 -*- coding: UTF-8 -*-
@date: 2019/8/30 21:29 
@name: 英制单位和公制单位互换.py
@author：Spring
"""

value = float(input('请输入长度:'))
uint = input('请输入单位:')
if uint == 'in' or uint == '英寸':
    print('%.2f英寸=%.2f厘米' % (value, value * 2.54))
elif uint == 'cm' or uint == '厘米':
    print('%.2f厘米=%.2f英寸' % (value, value / 2.54))
else:
    print('请输入正常的单位')
