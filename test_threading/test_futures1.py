#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/10 13:53
@File    : test_futures.py
@Author  : frank.chang@shoufuyou.com

线程池  是什么?

为什么 需要线程池?



线程池的两种提交方式,  submit   , map

区别,  相似点, 局限性 有哪些.



ThreadPoolExecutor 源码分析   https://www.jianshu.com/p/b9b3d66aa0be


"""

from concurrent.futures import ThreadPoolExecutor, as_completed,wait

import time


def get_html(seconds):
    time.sleep(seconds)

    # print(f"get_html {seconds} success.")
    return seconds


executor = ThreadPoolExecutor(max_workers=2)

seconds = [1, 2, 4, 5, 2, 3, 1]
# all_task = [executor.submit(get_html, second) for second in seconds]
#
# for future in as_completed(all_task):
#     result = future.result()
#
#     print(f"get_html({result}) done")


for data in executor.map(get_html, seconds):
    result = data
    print(f"get_html({result}) done")

if __name__ == '__main__':
    pass
