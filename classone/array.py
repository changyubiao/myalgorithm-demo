#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/7 23:05
@File    : array.py
@Author  : frank.chang@shoufuyou.com

给定一个数组 array    和一个数num

1.
给定一个数组arr， 和一个数num， 请把小于等于num的数放在数
组的左边， 大于num的数放在数组的右边。
要求额外空间复杂度O(1)， 时间复杂度O(N)



2.
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
            pass
            array[more - 1], array[cur] = array[cur], array[more - 1]
            more = more - 1
        else:  # ==num
            cur = cur + 1

    return less + 1, more - 1


def partition1(array, low, high, num):
    """
    # 基准点定位为第一个元素
    :param array:
    :param low:
    :param high:
    :param num:
    :return:
    """
    point = num

    while low < high:
        # 将大于基准点的数放于基准点的右边
        while low < high and array[high] >= point:
            # 移到前一个元素
            high = high - 1
        # 当不满足大于基准点，交换基准点
        array[low], array[high] = array[high], array[low]

        while low < high and array[low] < point:
            low = low + 1
        # 当不满足小于基准点，交换基准点
        array[low], array[high] = array[high], array[low]
    # 返回枢轴的位置。。。重要
    return low


if __name__ == '__main__':

    array = [1, 21, 34, 12, 4, 5, 10, 10, 6, 17, 10, 10, 8, 14]
    num = 10

    L = 0
    R = 11

    ret = partition(array, L, R, num=num)

    print(f"num:{num}, ret:{ret}")
    print(array)


