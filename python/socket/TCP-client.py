# -*- coding:utf-8 -*-

import socket

def tcp_client():
    # 1.建立socket通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接对方请求给对方通信
    addrs = ('127.0.0.1', 7652)
    sock.connect(addrs)

    # 3.发送内容给服务端
    msg = '客户端进行请求啦...'
    sock.send(msg.encode())

    # 4.接收对方的反馈
    data = sock.recv(200)
    data = data.decode()
    print(data)

    # 5.关闭链路通道
    sock.close()

if __name__ == '__main__':
    print('start..........')
    tcp_client()