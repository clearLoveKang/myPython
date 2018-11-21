# -*- coding:utf-8 -*-

'''
守护线程daemon

'''
import time
import threading

def func():
    print('start func')
    time.sleep(2)
    print('end func')

print('Main begin')

t1 = threading.Thread(target=func, args=())

# 设置一个守护线程 必须在子线程启动前设置
t1.setDaemon(True)
#t1.daemon = True
t1.start()
time.sleep(1)
print('Main Tread end')