# -*- coding:utf-8 -*-
'''
    UDP客户端程序
    1 建立socket通信
    2 发送内容到服务器
    3 接收服务器的返回信息

'''

import socket

def udp_client():

    # 建立socket通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 编辑发送到服务器的内容
    text = '我要请求你了!'
    data = text.encode()
    #发送
    sock.sendto(data, ('127.0.0.1', 7653))


    # 接收服务器返回信息
    info,addr = sock.recvfrom(200)

    detail = info.decode()
    print(detail, addr)


if __name__ == '__main__':
    udp_client()