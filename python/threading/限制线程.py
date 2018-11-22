# -*- coding:utf-8 -*-
import threading
import time

'''
    semaphore
    最多有几个线程执行
'''

# 设置可以有几个线程在执行
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print('正在执行的线程', threading.currentThread().getName())
        time.sleep(15)
        semaphore.release()
        print('正在执行的线程', threading.currentThread().getName())

for i in range(8):
    t1 = threading.Thread(target=func, args=())
    t1.start()