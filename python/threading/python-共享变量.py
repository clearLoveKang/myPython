# -*- coging:utf-8 -*-

import threading
'''
    共享资源使用时需要上锁
'''
sum = 0
loopSum = 100000
# 申请一把锁
lock = threading.Lock()

def add():
    global sum, loopSum
    for i in range(1, loopSum):
        # 使用前上锁
        lock.acquire()
        sum += 1
        # 使用后需要解锁释放
        lock.release()


def sub():
    global sum, loopSum
    for i in range(1, loopSum):
        # 使用前上锁
        lock.acquire()
        sum -= 1
        # 使用后解锁
        lock.release()


def main():
    print(sum)
    t1 = threading.Thread(target=add, args=())
    t2 = threading.Thread(target=sub, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(sum)

if __name__ == '__main__':
    main()