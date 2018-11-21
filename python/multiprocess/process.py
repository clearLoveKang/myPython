# -*- coding:utf-8_-*-

# 多进程
from time import ctime, sleep
import multiprocessing

def clock(interval):
    while True:
        print('this time is :', ctime())
        sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(4,))
    p.start()
    while True:
        sleep(1)