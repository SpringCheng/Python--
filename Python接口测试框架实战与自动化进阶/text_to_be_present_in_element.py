"""
判断文本：
判断某个元素中是否存在指定的文本
比如：登录后判断页面中的账号是否是该用户的用户名
@date: 2019/9/11 19:08 
@author：Spring
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# locator参数是定位方法
locator = ('id', 's_username_top')
# text是期望值
text = u'程平锟'
# 判断id=s_username_top的元素是否存在text的值
result = EC.text_to_be_present_in_element(locator, text)
print(result(driver))

time.sleep(10)
driver.close()

