#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/10 15:27
@File    : test_futures_demo3.py
@Author  : frank.chang@shoufuyou.com
"""
from concurrent.futures import ThreadPoolExecutor
import time

all_list = range(100)


def fun(num):
    print(f'fun({num}) begin sleep 4s ')
    time.sleep(4)
    return num + 1


with ThreadPoolExecutor() as executor:
    for result in executor.map(fun, all_list):
        print(f"result:{result}")
