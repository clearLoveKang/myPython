# -*- coding:utf-8 -*-

import time
import threading

# 重新定义的类继承自 threading.Thread

class myThread(threading.Thread):

    def __init__(self, args):
        super(myThread, self).__init__()
        self.args = args

    def run(self):
        time.sleep(2)
        print('the args for this class is {0}'.format(self.args))


for i in range(5):
    t = myThread(i)
    t.start()
    t.join()

print('全部结束了....')