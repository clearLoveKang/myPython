# -*- coding:utf-8 -*-

from multiprocessing import Process
import os

def info(title):
    print(title)
    # 先打印函数名称
    print('函数名称', __name__)
    # 打印父进程ID
    print('父进程ID:{0}'.format(os.getppid()))
    # 打印子进程ID
    print('当前进程ID{0}'.format(os.getpid()))


def func(name):
    info('func调用')
    print('z这是:',name)


if __name__ == '__main__':
    info('主进程执行')
    # 开一个子进程
    p = Process(target=func, args=('新开的子进程',))
    p.start()
    p.join()
    print('主进程结束')