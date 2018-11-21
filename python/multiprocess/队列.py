# -*- coding: utf-8 -*-

import multiprocessing
from time import ctime

def consumer(input_q):
    print('Into consumer:', ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item == None:
            break
        print('pull', item, 'out of q') # 消费者每次从队列q拿出的东西
        input_q.task_done() # 发出信号通知任务完成
    print('Out of consumer:', ctime())


def producer(sequence, output_q):
    print('Into producer:', ctime())
    for item in sequence:
        output_q.put(item) # 每次从仓库取出东西放入队列q
        print('put', item, 'in to q')

    print('Out of producer:', ctime()) # 生产者吧商品全部放入队列


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    # cons_p.daemon()设置守护进程
    cons_p.start()

    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    # cons_p.daemon()设置守护进程
    cons_p1.start()

    # 生产者多各项sequence代表要发出给消费者的项序列
    # 在实践中,这可能是生成器的输出或者通过一些其它方式生产出来
    sequence = [1,2,3,4,5,6]
    producer(sequence, q)

    # 设置哨兵 往仓库扔一个特殊值告知消费者看到这个就不能够在进行消费了 没有东西了
    # 有几个子进程 就要设置几个哨兵
    q.put(None)
    q.put(None)
    # JoinableQueue的好处就是可以等
    q.join()

