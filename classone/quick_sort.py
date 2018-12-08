#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/8 17:14
@File    : quick_sort.py
@Author  : frank.chang@shoufuyou.com
"""

"""
用荷兰国旗  问题 ， 改进  partition 过程

改进快速排序 

 

"""


def partition(array, L, R):
    """

    :param array:
    :param L:
    :param R:
    :return:  返回与num 相等 两个边界的index，
    """
    less = L - 1
    more = R  # 注意这里的写法
    cur = L

    # 用这个值 作为划分  array[R]  作为划分point 进行划分
    # num = array[R]

    while cur < more:
        if array[cur] < array[R]:
            array[less + 1], array[cur] = array[cur], array[less + 1]
            cur = cur + 1
            less = less + 1
        elif array[cur] > array[R]:
            pass
            array[more - 1], array[cur] = array[cur], array[more - 1]
            more = more - 1
        else:  # ==array[R]
            cur = cur + 1

    array[more], array[R] = array[R], array[more]
    return less + 1, more - 1


def quick_sort(array, low, high):
    if low < high:
        point_left, point_right = partition(array, low, high)
        print(f"array:{array}, point_left:{point_left},point_right:{point_right}")
        quick_sort(array, low, point_left - 1)
        quick_sort(array, point_right + 1, high)


if __name__ == '__main__':
    pass
    mylists = [8, 10, 9, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    quick_sort(mylists, 0, len(mylists) - 1)
    print(mylists)
