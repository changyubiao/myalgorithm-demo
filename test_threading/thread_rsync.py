#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/9 17:11
@File    : thread_rsync.py
@Author  : frank.chang@shoufuyou.com


线程如何同步 呢



什么叫线程 同步  ?


为什么 线程 同步


如何使用锁呢?
1 加锁会影响 性能, 要获取锁和释放锁.
2 有可能会引起 死锁. ... (Notice)
3

    A(a,b)
    acquire  a
    acquire  b


    B (b,a)
    acquire(b)
    acquire(a)




RLock     , 可重入锁 .

在同一个线程的里面, ,可以连续 调用多次 acquire ,  一定要注意 , 一定要注意相同次数的release



"""

import threading

from threading import Semaphore, BoundedSemaphore

from threading import Lock,RLock

total = 0

lock = Lock()


def add(lock):
    global total

    for i in range(100_0000):
        with lock:
            total += 1


def desc(lock):
    global total

    for i in range(100_0000):

        lock.acquire()

        # 死锁 情况..
        dosomethin(lock)

        lock.release()



def  dosomethin(lock):
    lock.acquire()

    # do sth
    lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"total:{total}")


"""
1  load  a
2  load 1 
3  + 
4   赋值给a  



-------------

1  load  a
2  load 1 
3   -
4   赋值给a  


加锁 

事务 一致性, 事务来解决这问题..



"""


if __name__ == '__main__':
    pass
