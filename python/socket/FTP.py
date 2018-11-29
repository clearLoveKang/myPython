# -*- coding:utf-8 -*-

import ftplib
import os
import socket

HOST = 'ftp.acc.umu.se'
DIR = 'Public/EFLIB'
FILE = 'README'

# 1.ftp连接远程主机
try:
    f = ftplib.FTP()

    #通过设置调试级别方便调试
    f.set_debuglevel(2)

    # 连接主机
    f.connect(HOST)

except Exception as e:
    print(e)
    exit()

print('***Connected to host {0}'.format(HOST))

# 2.进行登录
try:
    f.login()

except Exception as e:
    print(e)
    exit()

print('***Login*****')

# 3.客户端与主机进行信息交互找到目录
try:
    f.cwd(DIR)

except Exception as e:
    print(e)
    exit()

print('***change dir to {0}*****'.format(DIR))

# 4.从目录下载文件
try:
    f.retrbinary('RETR {0}'.format(FILE), open(FILE, 'wb').write)
except Exception as e:
    print(e)
    exit()


f.quit()
