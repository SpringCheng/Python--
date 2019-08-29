"""
输入半径计算圆的周长和面就
 -*- coding: UTF-8 -*-
@date: ${DATE} ${TIME}
@name: ${NAME}.py
@author：Spring
"""
# 周长:L=2πr
# 面积:S=πr**2

import math

radius = float(input('请输入圆的半径'))
Perimeter = 2 * math.pi * radius
Area = math.pi * radius * radius
print('圆的周长是:%.2f' % Perimeter)
print('圆的面积是:%.2f' % Area)
