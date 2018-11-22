# -*- coding:utf-8 -*-

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def fun1():
    print('fun1一开始工作')
    lock1.acquire()
    print('fun1申请了锁1')
    time.sleep(2)
    print('fun1睡了两秒')
    lock2.acquire()
    print('fun1申请了锁2')
    lock2.release()
    print('fun1释放了锁2')
    lock1.release()
    print('fun1释放了锁1')

def fun2():
    print('fun2一开始工作')
    lock2.acquire()
    print('fun2申请了锁2')
    time.sleep(4)
    print('fun2沉睡了4秒')
    lock1.acquire()
    print('fun2申请了锁1')
    lock1.release()
    print('fun2释放了锁1')
    lock2.release()
    print('fun2释放了锁2')

if __name__ == '__main__':

    t1 = threading.Thread(target=fun1, args=())
    t2 = threading.Thread(target=fun2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
