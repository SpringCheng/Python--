# coding:utf-8

from selenium import webdriver
# 导入expected_conditions（预期条件）
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image

# 选择chrome浏览器打开
driver = webdriver.Chrome()
# 打开5itest网址
driver.get("http://www.5itest.cn/register")

# 判断title是不是注册
# title=EC.title_is('注册账号')
# 判断title是否包含“注册”这两个字
# title=EC.title_contains('注册')
# print(title(driver))


# 判断controls元素是否显示出来了,然后再做后面的查找定位操作  （WebDriverWait，Unit，By.CLASS_NAME）
locator = (By.CLASS_NAME, "controls")
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))

# 获取输入框中输入的信息和本来的信息 （get_attribute方法获取属性值）
email_element=driver.find_element_by_id('register_email')
print(email_element.get_attribute('placeholder'))
email_element.send_keys('test@163.com')
print(email_element.get_attribute('value'))

# 随机生成注册邮箱
for i in range(5):
    # sample() 随机输出N个元素，返回列表
    # 第一个参数为列表，第二个参数为输出的个数
    user_email = ''.join(random.sample('12323sdsadfty56', 5))+"@163.com"
    print(user_email)


# 解析验证码
driver.save_screenshot("D:/imooc.png")
code_element=driver.find_element_by_id('getcode_num')
print(code_element.location)
# 图片定位
left=code_element.location['x']  # {'x': 538, 'y': 523}
top=code_element.location['y']
right=code_element.size["width"]+left
height=code_element.size["height"]+top
# 剪切图片
im=Image.open("D:/imooc.png")
img=im.crop((left,top,right,height))
img.save("D:/imooc1.png")
# 读取图片内容




# 不同的方式定位
# 根据id定位
# driver.find_element_by_id('register_email').send_keys('mushishi_01@163.com')
# time.sleep(10)
# # 根据class_name定位
# user_name_element_node = driver.find_elements_by_class_name('controls')[1]
#
# user_element = user_name_element_node.find_element_by_class_name('form-control')
#
# user_element.send_keys("cheng")
#
# # 根据name定位
# driver.find_element_by_name('password').send_keys('111111')
# time.sleep(5)
# # 根据xpath定位
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys('111111')
# time.sleep(7)

time.sleep(5)
driver.close()
