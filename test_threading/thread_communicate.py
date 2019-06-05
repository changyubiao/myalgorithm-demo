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


def get_detail_html(detail_url_list):
    # 抓取详情页

    # global detail_url_list

    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print(f"get_detail html startd {url}")
            time.sleep(2)

            print("get_detail html end")


def get_detail_url(detail_url_list):
    # 获取文章 列表页
    print("get_detail_url html startd")
    # global detail_url_list

    while True:
        for i in range(20):
            detail_url_list.append(f"http://xxx.com/{i}")

        time.sleep(5)


if __name__ == '__main__':

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))

    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))

        html_thread.start()
