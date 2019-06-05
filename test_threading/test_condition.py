#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/10 09:52
@File    : test_condition.py
@Author  : frank.chang@shoufuyou.com


测试 condition

acquire([timeout])/release(): 调用关联的锁的相应方法。
 with cond:
    pass


wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。

notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；
        其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。
            使用前线程必须已获得锁定，否则将抛出异常。




"""

import threading
from threading import Condition


from  threading import Semaphore,BoundedSemaphore

class XiaoAi(threading.Thread):

    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            self.cond.wait()
            print(f"{self.name}: 在呢")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name}: 好啊.")
            self.cond.notify()

            for num in range(2, 11, 2):
                self.cond.wait()
                print(f'{self.name}: {num} ')
                self.cond.notify()


class TianMao(threading.Thread):

    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            print(f'{self.name}: 小爱同学')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 我们来数数吧')
            self.cond.notify()
            self.cond.wait()

            for num in range(1, 10, 2):
                print(f'{self.name}: {num}')
                self.cond.notify()
                self.cond.wait()

            # self.cond.notify_all()


if __name__ == '__main__':
    cond = Condition()

    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 启动 顺序 很重要
    # 调用 with cond 之后, 才能调用  wait  ,notify 方法  ,这两个方法 必须拿到锁之后 才能使用.
    #  condition  有两层锁,一把底层锁会在线程调用了 wait 方法的时候释放, 上面的锁会在每次调用wait方法时候,分配一把,并方式 到cond 队列,等待 notify 唤醒.
    xiaoai.start()
    tianmao.start()
