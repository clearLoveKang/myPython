# -*- coding:utf-8 -*-

from time import ctime
import multiprocessing

def consumer(q):
    print('消费者开始消费:', ctime())
    while True:
        item = q.get()
        if item == None:
            print('队列已经空了别搞了.....')
            break
        print('队列取出来的是', item, ctime())
    q.task_done()
    print('老子把货全部取完了',ctime())


def producer(bom,q):
    print('生产者开始生产', ctime())
    for i in bom:
        q.put(i)
        print('放入队列生产的', i, ctime())
    print('老子吧货全部放进去了')


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    pro = multiprocessing.Process(target=consumer, args=(q,))
    pro.start()

    bomm = [1,2,3,4,5]
    producer(bomm,q)

    q.put(None)
    q.join()