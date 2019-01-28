#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/8 18:05
@File    : test_find_value.py
@Author  : frank.chang@shoufuyou.com



寻找 最接近的一个数,在已经排好序的数组中,    有一个数字 target 寻找  数组中与 target 的最近的数字

-------------------------------------------------
for example


array = [1.2, 2.1, 3, 3.5, 4, 4.3, 4.7, 5, 6, 7, 8, 9, 12]

target=5.1 , result: 5
target=5.7 , result: 6

target = 0    , result :  1.2
target = 15   , result :  12





"""


def find_interval(needle, array):
    """

    :param needle:
    :param array: len(array)  >=2
    :return:
    """

    max_index = len(array) - 1

    range_interval = {
        "left": -1,
        "right": -1
    }
    if len(array) == 2:
        range_interval["left"] = 0
        range_interval["right"] = 1
        return range_interval

    if needle <= array[0]:
        range_interval["right"] = 0
        return range_interval

    if needle >= array[-1]:
        range_interval["left"] = max_index
        return range_interval

    left, right = 0, max_index

    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        print(f"mid:{mid}  left:{left},right:{right}")
        if array[mid] == needle:
            break
        # 左半边
        elif array[mid] > needle:
            right = mid - 1
        # 右半边
        else:
            left = mid + 1

    # print(f"mid:{mid}")
    mid_value = array[mid]

    if mid_value > needle:
        range_interval['left'] = mid - 1
        range_interval['right'] = mid
    elif mid_value < needle:
        range_interval['left'] = mid
        range_interval['right'] = mid + 1
    else:
        range_interval['left'] = mid
        range_interval['right'] = mid
    return range_interval


def find_nearest_number(needle, array):
    """

    :param needle:
    :param array:
    :return:
    """
    interval = find_interval(needle, array)

    print(f"interval:{interval}")

    if interval['right'] == -1:
        return array[interval['left']]

    if interval['left'] == -1:
        return array[interval['right']]

    left_value = array[interval['left']]
    right_value = array[interval['right']]

    left_diff = abs(needle - left_value)
    right_diff = abs(needle - right_value)

    ret = left_value if left_diff <= right_diff else right_value
    return ret


if __name__ == '__main__':
    pass
    array = [1.2, 2.1, 3, 3.5, 4, 4.3, 4.7, 5, 6, 7, 8, 9, 12]
    target = 15

    ret = find_nearest_number(target, array)

    print(f"result:{ret}")
