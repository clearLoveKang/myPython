# -*- coding:utf-8 -*-
'''
现在使用的多线程模块
threading
用法 thd = threading.Thread(target=func, args=(xxx,))
      thd.start()
      thd.join() 主线程等待所有线程完成后才执行完成
守护线程daemon
    如果在程序中主线程挂了 子线程也随之挂掉
    守护线程中不允许 子线程独立运行
    Python-daemon.py
'''
import time
import threading

def loop1(name):
    print('loop1 {1} start work{0}'.format(time.ctime(), name))
    time.sleep(3)
    print('loop1 end work{0}'.format(time.ctime()))

def loop2(name):
    print('loop2 {1} start work{0}'.format(time.ctime(), name))
    time.sleep(4)
    print('loop2 end work{0}'.format(time.ctime()))

def mains():
    print('main start ...{0}'.format(time.ctime()))
    th1 = threading.Thread(target=loop1, args=('第一个', ))
    th2 = threading.Thread(target=loop2, args=('第二个', ))
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print('main end ...{0}'.format(time.ctime()))


if __name__ == '__main__':
    mains()