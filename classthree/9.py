#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/5 10:48
@File    : 9.py
@Author  : frank.chang@shoufuyou.com



在行列都排好序的矩阵中找数
【 题目】 给定一个有N*M的整型矩阵matrix和一个整数K，
matrix的每一行和每一 列都是排好序的。 实现一个函数， 判断K
是否在matrix中。


 例如： 0 1 2 5
       2 3 4 7
       4 4 4 8
       5 7 7 9



如果K为7， 返回true
如果K为6,  返回false

m1 = np.array([
    [0, 1, 2, 5],
    [2, 3, 4, 7],
    [4, 4, 4, 8],
    [5, 7, 7, 9]]
)

【 要求】 时间复杂度为O(N+M),额外空间复杂度为O(1).

"""

import numpy as np


def find_targe(matrix, target):
    """

    判断  target  是否 在 matrix

    返回  True  or  False
    :param matrix:
    :param target: int
    :return: True or False

    从右上角开始找.
    """

    row, column = matrix.shape

    start = 0, column - 1

    i, j = start
    flag = False

    # 控制  左边界, 和下边界,
    # 让起点 从 右上角开始
    while i != row and j != -1:
        if matrix[i][j] > target:
            # 往左找
            j = j - 1
        elif matrix[i][j] < target:
            # 往下找
            i = i + 1
        else:
            # equal 找到值.
            flag = True
            return flag

    return flag


def find_targe2(matrix, target):
    """

    判断  target  是否 在 matrix
    返回  True  or  False
    :param matrix:
    :param target: int
    :return: True or False

    从左下角 开始 找 ...
    """

    row, column = matrix.shape

    start = row - 1, 0

    i, j = start
    flag = False

    # 控制 右边界和上边界
    # 让起点 从 左下角开始
    while i != -1 and j != column:
        if matrix[i][j] > target:
            # 往 上找
            i = i - 1
        elif matrix[i][j] < target:
            # 往 右找
            j = j + 1
        else:
            flag = True
            return flag
    return flag


if __name__ == '__main__':
    matrix = np.array([
        [1, 3, 5, 6],
        [2, 5, 7, 9],
        [4, 6, 8, 10],
    ])

    target = 19
    ret = find_targe2(matrix, target)
    print(f"ret:{ret}")
    pass
