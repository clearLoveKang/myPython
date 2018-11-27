# -*- coding:utf-8 -*-

'''
    TCP 客户端程序
    1 建立socket负责具体通信
    2 绑定 IP 端口
    3 监听接入的访问socket
    4 接收访问的socket,接受访问即建立了一个通信的 链路通道
    5 接收对方内容
    6 如果有必要返回信息给对方
    7 关闭链路通道

'''
import socket
def tcp_srv():

    # 建立socket通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP 端口
    addrs = ('127.0.0.1', 7652)
    sock.bind( addrs )


    # 监听socket
    sock.listen()
    while True:
        # 建立链路通道
        skt,addr = sock.accept()

        # 接收对方内容
        data = skt.recv(500)
        data = data.decode()
        print(data, addr)

        rsp = '接收到服务端回复了'
        rsp = rsp.encode()

        # 发送信息返给客户端
        skt.send(rsp)

        # 关闭链路通道
        skt.close()

if __name__ == '__main__':
    print('start......')
    tcp_srv()