#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/9 16:07
@File    : python_gil.py
@Author  : frank.chang@shoufuyou.com



python  中的

global


CPython 解释器的实现
GIL  使得 同一时刻 只有一个线程 在一个cpu 上执行字节码,  无法将多个线程  映射到 多个CPU 上 .


gil  会根据 字节码行数, 以及 时间片 , 释放 gil

gil  遇到IO 操作 的时候 ,这个时候  锁会被释放掉. 让给其他线程.




# def add(a):
#     a = a + 1
#
#     return a
#
# print(dis.dis(add))

"""

import threading
import dis

total = 0


def add():
    global total

    for i in range(100_0000):
        total += 1


def desc():
    global total
    for i in range(100_0000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"total:{total}")

if __name__ == '__main__':
    pass
