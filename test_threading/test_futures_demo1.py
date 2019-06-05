#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/10 15:27
@File    : test_futures_demo1.py
@Author  : frank.chang@shoufuyou.com
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random


def sleep(s):
    time.sleep(s * 0.1)
    return s


if __name__ == '__main__':

    wait_for = []
    executor = ThreadPoolExecutor(4)
    l = list(range(10))
    random.shuffle(l)
    for seconds in l:
        future = executor.submit(sleep, seconds)
        wait_for.append(future)
        print('Scheduled for {}:{}'.format(seconds, future))

    results = []

    for f in as_completed(wait_for):
        res = f.result()
        msg = '{} result:{!r}'
        print(msg.format(f, res))
        results.append(res)

    print(l)
    print(results)


"""
看结果返回 是无序的,和任务提交的不一样的顺序的. 
"""