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

from_addr = '867912954@qq.com'
password = 'ukvntrhvvtugbcii'

# 收件方信息
to_addr = '1758661453@qq.com'


# 发信服务器
smtp_server='smtp.qq.com'
smtp_port=465

msg=MIMEText('sen by python','plain','utf-8')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, smtp_port)



try:
    # 登录邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr,to_addr,msg.as_string())
    # 关闭服务器
    server.quit()
    # server.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error,邮件发送错误')
