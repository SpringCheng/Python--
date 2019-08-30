"""
在send email基础上实现邮件群发

 -*- coding: UTF-8 -*-
@date: 2019/8/30 17:07 
@name: 邮件群发1.py
@author：Spring
"""
# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 用于构建邮件头
from email.header import Header
# 引用csv模块，用于读取邮箱信息
import csv

# 发件方服务器配置信息
smtp_server = 'smtp.qq.com'
smtp_port = 465

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)


# 发件方地址
from_addr = '867912954@qq.com'
# from_addr=input('请输入发件人邮箱:')
password = input('请输入邮箱密码:')

# 收件人信箱地址
to_addres = ['1758661453@qq.com', 'springcc.cheng@gmail.com', 'springcc_cheng@163.com']

# 邮件头部信息
sub = '这是Python邮件的测试项目'  # 主题

# 邮箱正文内容，第一个参数为内容，第二个参数为格式，第三个为编码
content = '''应用场景 迄今为止，
我们写的Python代码都是一条一条语句顺序执行，
这种代码结构通常称之为顺序结构。然而仅有顺序结构并不能
解决所有的问题，邮件群发1'''

# 使用MIMEText类创建实例，发送文本类型的邮件
msg = MIMEText(content, 'plain', 'utf-8')

try:
    # 登录邮箱
    server.login(from_addr, password)
    # 连接邮箱
    server.connect(smtp_server, smtp_port)

    # 邮件头部信息
    msg['From'] = Header(from_addr)

    """
    方式1 设置一个列表形式的变量
    Header()第一个参数数据类型必须为字符串或者字节，不能解码。
    join()用法是str.join(sequence),str代表这些字符串之间用干什么字符串来连接
    msg['To'] = Header(",".join(header_toer))
    """

    msg['To'] = Header("-".join(to_addres))
    msg['Subject'] = Header(sub)

    # 发送邮件
    server.sendmail(from_addr, to_addres, msg.as_string())
    # 关闭服务器
    server.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error,邮件发送错误')
