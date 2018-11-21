# -*- coding:utf-8 -*-

# 多线程
# thread 老版的多线程类
# 可以带参数 用法 _thread.start_new_thread(func, args)
import _thread as thread
import time

def loop1(name):
    print('loop1 {1} start work{0}'.format(time.ctime(), name))
    time.sleep(3)
    print('loop1 end work{0}'.format(time.ctime()))

def loop2(name):
    print('loop2 {1} start work{0}'.format(time.ctime(), name))
    time.sleep(4)
    print('loop2 end work{0}'.format(time.ctime()))

def main():
    print('main start ...{0}'.format(time.ctime()))
    thread.start_new_thread(loop1, ('第一个', ))
    thread.start_new_thread(loop2, ('第二个', ))
    print('main end ...{0}'.format(time.ctime()))


if __name__ == '__main__':
    main()
    while True:
        time.sleep(5)

