# -*- coding:utf-8 -*-
from time import sleep, ctime
import threading

def func():
    print('i am running...')
    sleep(4)
    print('i am dene ...')

if __name__ == '__main__':
    t = threading.Timer(6, func)
    t.start()

    n = 0
    while True:
        print('{0}........'.format(n))
        sleep(3)
        n += 1