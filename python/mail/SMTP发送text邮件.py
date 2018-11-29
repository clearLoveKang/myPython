# -*- coding:utf-8 -*-

import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Hello DanDan,I came to see you', 'plain', 'utf-8')

from_addr = input('From: ')
from_pwd = input('Password: ')
to_addr = input('addr: ')
smtp_srv = 'smtp.qq.com'

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)






