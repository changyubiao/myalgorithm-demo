#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/14 15:20
@File    : heap_sort.py
@Author  : frank.chang@shoufuyou.com


堆排序



"""

import random


def heap_ajust(array, start, end):
    """
    调整堆，变成一个大顶堆
    :param array:
    :param start:
    :param end:
    :return:
    """
    dad = start
    son = 2 * dad + 1

    while (son <= end):
        # 寻找最大的son
        if son + 1 <= end and array[son] < array[son + 1]:
            son = son + 1

        if (array[dad] > array[son]):
            return
        else:
            array[dad], array[son] = array[son], array[dad]
            dad = son
            son = 2 * dad + 1


def heap_sort(array, length):
    pass

    # 建堆
    for i in range(length // 2 - 1, -1, -1):
        heap_ajust(array, i, length - 1)

    # 先将第0個元素和最后一个元素交换值，之后在 待排序列中 进行 堆调整，直到i=1排序完毕
    for i in range(length - 1, 0, -1):
        # 和堆顶元素交换
        array[0], array[i] = array[i], array[0]

        # 继续调整堆
        heap_ajust(array, 0, i - 1)




if __name__ == '__main__':
    pass
    mylists = [8, 10, 9, 6, 46, 5, 13, 26, 18, 34, 23, 1, 7, 3]

    random.shuffle(mylists)
    print(mylists)

    heap_sort(mylists, len(mylists))
    print(mylists)
