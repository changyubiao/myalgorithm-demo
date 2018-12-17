#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 09:35
@File    : bubble_sort.py
@Author  : frank.chang@shoufuyou.com



# 冒泡排序的实现
'''''交换排序—冒泡排序（Bubble Sort）'''


"""
import random


def __bubble_sort(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort(array):
    length = len(array)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    mylist = [1, 34, 6, 21, 98, 31, 7, 4, 36, 16, 47, 67, 37, 25, 2]

    expect_list = mylist.copy()

    expect_list.sort()


    random.shuffle(mylist)
    print(mylist)
    bubble_sort(array=mylist)


    print(mylist)
    print(mylist == expect_list)

    # print(expect_list)



