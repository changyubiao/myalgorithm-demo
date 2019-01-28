#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/9 14:54
@File    : test5.py
@Author  : frank.chang@shoufuyou.com
"""

import pandas as pd

import numpy as np

fun = lambda x: x + 1

fun2 = lambda x: x * 2

fun3 = lambda x: x * 3


def fun(x):
    return x + 1


df = pd.DataFrame(
    data=[
        [fun, fun2, fun3],
        [fun, fun2, fun3],
        [fun, fun2, fun3]
    ],
    columns=['col1', 'col2', 'col3']
)

print(df)
df2 = pd.DataFrame(np.arange(1, 10).reshape((3, 3)), columns=['col1', 'col2', 'col3'])

print(df2)


# df2.applymap()
# df3 = df2.apply(func=fun)

# print(df3)

if __name__ == '__main__':
    pass
