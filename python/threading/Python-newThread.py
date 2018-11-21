# -*- coging:utf-8 -*-

from time import sleep, ctime
import threading

loop = [4,2]

class ThreadFunc():

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        '''

        :param nloop: loop函数名称
        :param nsec: 系统休息时间
        :return:
        '''
        print('Start loop:', nloop, 'at', ctime())
        sleep(nsec)
        print('Done loop:', nloop, 'at', ctime())


def main():
    print('Starting at:', ctime())

    '''
        ThreadFunc('loop').loop == 下面两行
        t = ThreadFunc('loop')
        t.loop
    '''
    # 实例化ThreadFunc类 并给个名字叫loop
    # ThreadFunc 类需要一个参数 name
    t = ThreadFunc('loop')

    # 创建两个子进程 继承自ThreadFunc类的 loop方法
    # loop类方法需要两个参数
    t1 = threading.Thread(target= t.loop, args=('LOOP1', 4))
    t2 = threading.Thread(target= t.loop, args=('LOOP2', 2))

    # 开始两个进程
    t1.start()
    t2.start()

    # 告诉主线程 等我搞完在结束
    t1.join()
    t2.join()

    # 等所有进程结束就通知一下
    print('ALL done at:', ctime())



if __name__ == '__main__':
    main()