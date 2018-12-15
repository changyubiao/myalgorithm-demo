#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/7 23:05
@File    : array.py
@Author  : frank.chang@shoufuyou.com


问题二（荷兰国旗问题）
给定一个数组arr， 和一个数num， 请把小于num的数放在数组的
左边， 等于num的数放在数组的中间， 大于num的数放在数组的
右边。

"""


def partition(array, L, R, num):
    """
    返回 一个元祖
    荷兰国旗问题
    :param array:
    :param L:
    :param R:
    :param num:
    :return: 返回一个 num 相同位置的 index ,左边 index ,右边 index
    """
    less = L - 1
    more = R + 1
    cur = L

    while cur < more:

        if array[cur] < num:
            array[less + 1], array[cur] = array[cur], array[less + 1]
            cur = cur + 1
            less = less + 1
        elif array[cur] > num:
            array[more - 1], array[cur] = array[cur], array[more - 1]
            more = more - 1
        else:  # ==num
            cur = cur + 1

    return less + 1, more - 1


if __name__ == '__main__':
    array = [1, 21, 34, 12, 4, 5, 10, 10, 6, 10, 17, 10, 10, 8, 10, 14]
    num = 10

    L = 0
    R = len(array) - 1

    ret = partition(array, L, R, num=num)

    print(f"num:{num}, ret:{ret}")
    print(array)
