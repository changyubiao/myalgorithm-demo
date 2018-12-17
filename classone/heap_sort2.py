# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/14 16:28
@File    : heap_sort2.py
@Author  : frank.chang@shoufuyou.com


O(N) = log 1 + log 2 + .... + logN-1




python3  -1/2  == -0.5
         -1//2  = -1     ===>   如何处理这种问题呢...

import heapq

"""
import random


def heap_sort(array):
    length = len(array)

    if (not array) or (length < 2):
        return

    # 建堆 O（N)
    for i in range(0, length, 1):
        heap_insert(array, i)

    heap_size = length

    array[0], array[heap_size-1] = array[heap_size - 1], array[0]
    heap_size = heap_size - 1

    while heap_size > 0:
        heapify(array, 0, heap_size)

        array[0], array[heap_size - 1] = array[heap_size - 1], array[0]
        heap_size -= 1


def heapify(arr, index, heap_size):
    """
    调整堆的结构，使变成大顶堆
    :param arr:
    :param index:
    :param heap_size: 堆的大小
    :return:
    """
    left = index * 2 + 1

    while left < heap_size:  # 堆结构 是否要继续排序

        right = left + 1
        if right < heap_size and arr[right] > arr[left]:
            largest_idx = right
        else:
            largest_idx = left

        largest = largest_idx if arr[largest_idx] > arr[index] else index

        if largest == index:
            break

        arr[largest], arr[index] = arr[index], arr[largest]

        index = largest
        left = index * 2 + 1


def heap_insert(arr, index):
    """
    加入 节点 ,  往上调整（大顶堆）

                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12       13       14


    上面是一颗满二叉树， 比如小标

    i  -->  left= 2*i + 1,right = 2*i + 2


    如果知道 孩子节点小标 ，如何寻找 父节点的坐标呢？

    设 left = A    i = (A-1)//2  或者   (A-2)//2  对于 这两种情况 其实 合并成一种，
    如果这个数是奇数，刚好减一整除2 ，
    如果这个数是偶数  减一 除2 是 x.5  ,只要取整数部分就可以了。

    看图 举个例子：

    9 的父节点：  9-1/2 = 4   ;10的父节点  (10-1)//2= 4



    (index -1) //2   就是父节点的下标
    :param arr:
    :param index:
    :return:
    """
    while arr[index] > arr[(index - 1) // 2]:
        # swap
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2
        #
        if index <= 0:
            # print(f'{index} break')
            break

        # print(f"index:{index}")


if __name__ == '__main__':
    array = list(range(1, 50))
    # array = [10, 8, 7, 2, 3, 5, 4, 12]
    random.shuffle(array)
    print(array)

    heap_sort(array)

    # print(array)
    # heap_insert(array, 7)






    expect = list(range(1, 50))


    print(f"array == expect:{array == expect}")






    pass
