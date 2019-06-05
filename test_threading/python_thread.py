#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/9 16:24
@File    : python_thread.py
@Author  : frank.chang@shoufuyou.com



操作系统  可以调度的最小单元 线程


对于 IO 操作来说 ,  多线程 和多进程 性能 差别不大.


网络请求, socket 编程,爬虫


如何创建  线程




需求:

1 主线程 退出, 子线程退出  thread.daemon = True
       thread1.daemon=True
        thread2.daemon=True

2  子线程 join , 等待当前线程 ,等待 线程执行完成,才会继续执行.



多线程 创建的两种方式.

"""

import threading
import time
from typing import Optional, Callable, Any, Iterable, Mapping


def get_detail(url):
    print("get_detail html startd")

    time.sleep(2)

    print("get_detail html end")


def get_detail_url(url):
    print("get_detail_url html startd")

    time.sleep(5)

    print("get_detail_url html end")


# 继承类  创建 线程


class DeTailHtml(threading.Thread):

    def __init__(self, name) -> None:
        super().__init__(name=name)

    def run(self) -> None:
        print("get_detail html startd")

        time.sleep(2)

        print("get_detail html end")


class DeTailUrlHtml(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get_detail_url html startd")

        time.sleep(5)

        print("get_detail_url html end")


if __name__ == '__main__1111':
    # print("main thread end.")
    start = time.time()
    thread1 = threading.Thread(target=get_detail, args=('www.baidu.com',))
    thread2 = threading.Thread(target=get_detail_url, args=('www.baidu.com/item?id=10',))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # print("main thread end.")
    print(f"finish total time: {time.time()-start}")

if __name__ == '__main__':
    thread1 = DeTailHtml('DetailHtml')

    thread2 = DeTailUrlHtml('DetailUrlHtml')
    start = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # print("main thread end.")
    print(f"finish total time: {time.time()-start}")
