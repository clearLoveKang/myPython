# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('小可爱,起床吃饭饭啦', 'plain', 'utf-8')

from_addr = input('form')
from_pwd = input('password')
to_addr = input('addr: ')

msg['From'] = Header('大佬康<*******@qq.com>', 'utf-8')
msg['To'] = Header('小宝贝<*******@qq.com>', 'utf-8')
msg['Subject'] = Header('康康来看下小宝贝', 'utf-8')

smtp_srv = 'smtp.qq.com'

try:
    # 与邮箱服务器建立连接
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    # 打印交互过程
    srv.set_debuglevel(1)
    # 进行登录
    srv.login(from_addr, from_pwd)
    # 发送邮件 来自哪里 发到哪里 内容
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    # 退出
    srv.quit()

except Exception as e:
    print(e)



