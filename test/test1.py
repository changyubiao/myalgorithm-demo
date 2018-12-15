#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/10 17:00
@File    : test1.py
@Author  : frank.chang@shoufuyou.com


给定一个数组 array    和一个数num

1.
给定一个数组arr， 和一个数num， 请把小于等于num的数放在数
组的左边， 大于num的数放在数组的右边。

要求额外空间复杂度O(1)， 时间复杂度O(N)


"""


def partition1(array, L, R, num):
    """
    返回 一个元祖
    荷兰国旗问题
    :param array:
    :param L:
    :param R:
    :param num:
    :return: 返回一个 num
    """
    less = L - 1
    more = R + 1
    while L < more:

        if array[L] < num:
            array[less + 1], array[L] = array[L], array[less + 1]
            L = L + 1
            less = less + 1
        elif array[L] > num:
            array[L], array[more - 1] = array[more - 1], array[L]
            more = more - 1
        else:
            pass
            L = L + 1

    print(f"less:{less} ,more:{more}")
    return less


def partition(array, L, R, num):
    """
    请把小于等于num的数放在数组的左边，
     大于num的数放在数组的右边。(不要求顺序)

    荷兰国旗问题
    :param array:
    :param L:
    :param R:
    :param num:
    :return: 返回一个 num
    """
    less = L - 1
    more = R + 1
    cur = L

    while cur < more:

        if array[cur] <= num:
            array[less + 1], array[cur] = array[cur], array[less + 1]
            cur = cur + 1
            less = less + 1
        elif array[cur] > num:
            cur = cur + 1

    return less


if __name__ == '__main__':
    array = [1, 21, 34, 12, 4, 10, 5,10, 87, 10, 6,10, 17, 10, 14, 8, 14]
    num = 10

    L = 0
    R = len(array)-1

    pos = partition1(array, L, R, num=num)

    print(f"num:{num}, pos:{pos}, array[{pos}]:{array[pos]}")
    print(array)

    pass
