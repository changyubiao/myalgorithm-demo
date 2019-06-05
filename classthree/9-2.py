#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/5 10:48
@File    : 9.py
@Author  : frank.chang@shoufuyou.com


"""

import heapq
import random

if __name__ == '__main__':
    data = list(range(10, 20))

    random.shuffle(data)

    k = input("please intput your number: ")

    print(f"before:{data}")
    m = heapq.nlargest(int(k), data)

    print(m)
    print(m[-1])

    pass
