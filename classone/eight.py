#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/8 12:45
@File    : eight.py
@Author  : frank.chang@shoufuyou.com

小和问题
在一个数组中， 每一个数左边比当前数小的数累加起来， 叫做这个数组的小和。 求一个数组
的小和。
例子：
[1,3,4,2,5]
1左边比1小的数， 没有；
3左边比3小的数， 1；
4左边比4小的数， 1、 3；
2左边比2小的数， 1；
5左边比5小的数， 1、 3、 4、 2；
所以小和为1+1+3+1+1+3+4+2=16


"""


def solution(array):
    sum_ = 0
    for i, item in enumerate(array):

        for j in range(0, i + 1):
            if array[j] < array[i]:
                sum_ += array[j]
    return sum_


if __name__ == '__main__':
    pass
    # array = [9, 6, 2, 5, 7, 4, 1, 0, 3, 8]
    array = [1, 3, 4, 2, 5]

    # print(array)
    s = solution(array)

    print(f"sum:{s}")
