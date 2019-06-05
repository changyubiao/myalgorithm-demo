#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/9 17:11
@File    : thread_rsync.py
@Author  : frank.chang@shoufuyou.com


为什么 线程 同步

condition 条件变量  用于线程同步的锁.



condition 原理 介绍:
condition 实际上有两层锁, 一把锁 底层锁,会在 线程调用 wait 方法的时候释放.
上面的锁 会在在每次调用wait 方法的时候 ,分配一把锁,并且放入到cond 的等待队列中, 等其他线程 notify唤醒该线程.




注意 :
 调用 with cond 之后, 才能调用  wait  ,notify 方法  ,这两个方法必须拿到锁之后 才能使用.










小爱 和天猫精灵  之间的对话.


"""

import threading
from threading import Condition
import time

"""
天猫精灵 和小爱 同学对话.


 



"""


class XiaoAi(threading.Thread):

    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            for num in range(2, 10, 2):
                self.cond.wait()
                print(f'{self.name}: {num} ')
                self.cond.notify()

            # self.cond.notify_all()


class TianMao(threading.Thread):

    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
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
    #  condition  有两层锁, 一把底层锁会在线程调用了 wait 方法的时候释放, 上面的锁会在每次调用wait 方法 时候, 分配一把,并方式 到cond 队列,等待 notify 唤醒.
    xiaoai.start()
    tianmao.start()


    pass
