#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/10 13:53
@File    : test_futures.py
@Author  : frank.chang@shoufuyou.com

线程池  是什么?

为什么 需要线程池?


"""

from concurrent.futures import ThreadPoolExecutor

import time


def get_html(seconds):
    time.sleep(seconds)

    print(f"get_html {seconds} success.")

    return 'success'


executor = ThreadPoolExecutor(max_workers=2)

task1 = executor.submit(get_html, 2)
task2 = executor.submit(get_html, 4)
task3 = executor.submit(get_html, 6)


# 取消task3 , 只要task3 没有开始运行,是可以直接取消的.
task3.cancel()


print(f"task2.result(): {task2.result()}")


# print(f"task1.done():{task1.done()}")
# time.sleep(3)
#
# print(f"task1.done():{task1.done()}")
#
# print(f"task2.result(): {task2.result()}")  # 阻塞的方法
