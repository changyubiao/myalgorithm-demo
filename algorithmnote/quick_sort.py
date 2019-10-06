# -*- coding: utf-8 -*- 

from typing import List
import random

"""
quicksort  

A[1] ...    A[n] 对于这个序列


xxx  , A[1] ,... A[n] , 


保证 A[1] 左边的元素 都小于等于A[1],  保证A[1] 右边的元素 都大于 A[1]



chapter4 第四章 笔记 

"""


def partition(array: List, left: int, right: int) -> int:
    """

    :param array:
    :param left:
    :param right:
    :return:
    """

    # 临时变量
    temp = array[left]

    while left < right:
        # 这个 left < right 这个条件不能丢
        while left < right and array[right] > temp:
            right = right - 1

        # 把 小的数字放在左边
        array[left] = array[right]

        # 这个left < right 这个条件不能丢
        while left < right and array[left] <= temp:
            left = left + 1

        # 把大的数字 放到右边
        array[right] = array[left]

    array[left] = temp

    # print(f"left:{left}, right: {right}")
    return left


def quick_sort(array, left, right):
    if left < right:
        point = partition(array, left, right)
        quick_sort(array, left, point - 1)
        quick_sort(array, point + 1, right)


if __name__ == '__main__':
    # a = [i for i in range(10)]
    # random.shuffle(a)

    a = [6, 5, 7, 4, 0, 3, 9, 1, 2, 8]

    # a  = [1,2,3,4,5]
    left, right = 0, len(a) - 1

    print(a)

    pos = partition(array=a, left=0, right=len(a) - 1)

    print(pos)
    #

    # quick_sort(a,left,right)

    print('======' * 18)
    print(a)
    pass
