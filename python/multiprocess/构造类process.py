# -*- coding:utf-8 -*-

import multiprocessing
from time import ctime, sleep

class MyProcess(multiprocessing.Process):

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print('this time is:', self.interval)
            sleep(self.interval)



if __name__ == '__main__':
    p = MyProcess(5)
    p.start()
    while True:
        print('保持主进程不会挂掉',ctime())
        sleep(1)