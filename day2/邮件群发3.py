"""
在send email基础上实现邮件群发

 -*- coding: UTF-8 -*-
@date: 2019/8/30 17:07
@name: 邮件群发.py
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

# 发件方地址
from_addr = '867912954@qq.com'
password = input('请输入邮箱密码:')

# 邮件头部信息
sub = '这是Python邮件的测试项目'  # 主题

# 邮箱正文内容，第一个参数为内容，第二个参数为格式，第三个为编码
content = '''应用场景 迄今为止，
我们写的Python代码都是一条一条语句顺序执行，
这种代码结构通常称之为顺序结构。然而仅有顺序结构并不能
解决所有的问题，群发邮件3'''

# 收件人信箱地址

# 方法三  导入邮箱数据到csv文件
data = [['spring', 'springcc_cheng@163.com'], ['cheng', '1748661453@qq.com'], ['chun', 'springcc.cheng@gmail.com']]
# 写入收件人数据
with open('to_addres.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

try:
    # 读取收件人csv文件，并启动写信和发信的交流
    with open('to_addres.csv', 'r') as f:
        reader = csv.reader(f)  # 模块.方法( ) , reader()读取f文件内容到变量reader
        for row in reader:
            to_addres = row[1]
    # 使用MIMEText类创建实例，发送文本类型的邮件
    msg = MIMEText(content, 'plain', 'utf-8')
    # 邮件头部信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addres)
    msg['Subject'] = Header(sub)

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, smtp_port)
    # 登录邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addres, msg.as_string())
    # 关闭服务器
    server.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error,邮件发送错误')
