"""

@date: 2019/9/11 17:54 
@author：Spring
"""

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

# 打开谷歌浏览器
driver=webdriver.Chrome()
# 打开网址
driver.get('http://www.cnblogs.com/surewing')
# 实例化title对象，检查页面title和期望值(cherry小樱桃 - 博客园)是否完全一样
# 是就返回True，否返回False
# title是可调用对象
title = EC.title_is(u"cherry小樱桃 - 博客园")
# 实例化title对象，检查页面title是否包含期望值(如果)
# 是就返回True，否返回False
title1=EC.title_contains(u"如果")

print(title(driver))

time.sleep(12)
driver.close()

