# -*- coding:utf-8 -*-
'''
    多线程常用属性
        threading.currentThread 获取当前线程变量
        threading.enumerate: 返回一个包含正在运行线程的list
        threading.activeCount 返回正在运行线程数量
        thr.setName 设置线程名字
        thr.getName 获取线程名字
'''
import time
import threading

def loop1():
    print('loop1 start at:', time.ctime())
    time.sleep(4)
    print('loop1 end at:', time.ctime())


def loop2():
    print('loop2 start at:', time.ctime())
    time.sleep(2)
    print('loop2 end at:', time.ctime())


def loop3():
    print('loop3 start at:', time.ctime())
    time.sleep(5)
    print('loop3 end at:', time.ctime())


def main():
    print('main thread start at:', time.ctime())

    # 创建三个子进程 并进行命名
    th1 = threading.Thread(target=loop1, args=())
    th1.setName('oneThread')
    th1.start()

    th2 = threading.Thread(target=loop2, args=())
    th2.setName('twoThread')
    th2.start()

    th3 = threading.Thread(target=loop3, args=())
    th3.setName('threeThread')
    th3.start()

    # 子进行开始后我们就让主线程休息三秒
    time.sleep(3)

    # 然后我们获取到当前正在进行的线程程名字
    for th in threading.enumerate():
        print('{0} running ...'.format(th.getName()))

    # 打印正在运行线程程的个数
    print('thread number is {0}'.format(threading.activeCount()))

    # 提示整个进程结束
    print('all down at:', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)