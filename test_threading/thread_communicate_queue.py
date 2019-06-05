#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/9 16:42
@File    : thread_communicate.py
@Author  : frank.chang@shoufuyou.com


线程间 如何通信 呢?



线程间  为什么 需要通信 ?

1  共享变量

2  queue 队列



通过 global 共享变量的方式, 实现线程通信 .


"""

import threading
import time
from queue import Queue

detail_url_list = []


def get_detail_html(queue):
    # 抓取详情页

    while True:
        url = queue.get()
        print(f"get_detail html startd {url}")
        time.sleep(2)

        print("get_detail html end")


def get_detail_url(detail_url_list):
    # 获取文章 列表页
    print("get_detail_url html startd")

    while True:
        for i in range(20):
            detail_url_list.append(f"http://xxx.com/{i}")

        time.sleep(0.2)


if __name__ == '__main__':

    detail_url_queue = Queue(maxsize=100)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))

    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))

        html_thread.start()

    # detail_url_queue.task_done()
    # detail_url_queue.join()
