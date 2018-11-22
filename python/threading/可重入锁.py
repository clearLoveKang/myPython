# -*- coding:utf-8 -*-
import threading
from time import ctime, sleep

class MyThread(threading.Thread):
    def run(self):
        global num
        sleep(1)

        if mutex.acquire(1):
            num += 1
            msg = self.name+'set num to'+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0
#设置锁
# mutex = threading.Lock()
# 设置可重入锁
mutex = threading.RLock()

def fun():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    fun()