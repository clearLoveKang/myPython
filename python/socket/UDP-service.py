# -*- coding:utf-8 -*-

'''
    UDP服务端程序
    1 建立socket通道
    2 绑定地址 IP+端口
    3 接收客户端请求数据
    4 信息交换返回数据
'''
import socket

def udp_srv():
    # 建立socket请求
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # 绑定IP端口地址
    addrs = ('127.0.0.1', 7653)
    sock.bind( addrs )

    # 接收客户端发送的消息
    data, addr = sock.recvfrom(500)
    print(data.decode())

    # 对客户端进行反馈
    rsp = '你好! 我接收到你的消息了'
    rsp = rsp.encode()

    # 发送消息给客户端
    sock.sendto(rsp, addr)

if __name__ == '__main__':
    print('start....')
    while True:
        try:
            udp_srv()
        except Exception as e:
            print(e)
