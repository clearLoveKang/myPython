# -*- coding:utf-8 -*-

import time
import threading
import queue

# 生产者类
class Producer(threading.Thread):

    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count+1
                    msg = '生产者生产了'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


# 消费者类
class Consumer(threading.Thread):

    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
            time.sleep(1)


# 运行主函数
if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(500):
        queue.put('初始化产品'+str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()