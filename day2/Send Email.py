"""
自动化发送邮件

 -*- coding: UTF-8 -*-
@date: 2019/8/30 10:36 
@name: Send Email.py
@author：Spring
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发件方信息
from_addr = '867912954@qq.com'
password = input('请输入邮箱密码:')

# 发件方配置信息
smtp_server = 'smtp.qq.com'
smtp_port = 465

# 收件方信息
to_addr = '1758661453@qq.com'

# 邮件头部信息
header_former = 'springcccc'  # 发送人
header_Toer = 'cheng'  # 接收人
sub = '这是Python邮件的测试项目' # 主题

# 邮箱正文内容，第一个参数为内容，第二个参数为格式，第三个为编码
content='''应用场景 迄今为止，
我们写的Python代码都是一条一条语句顺序执行，
这种代码结构通常称之为顺序结构。然而仅有顺序结构并不能
解决所有的问题，'''


msg = MIMEText(content, 'plain', 'utf-8')


# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, smtp_port)

try:
    # 登录邮箱
    server.login(from_addr, password)

    # 邮件头部信息
    msg['From'] = Header(header_former)
    msg['To'] = Header(header_Toer)
    msg['Subject'] = Header(sub)

    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error,邮件发送错误')