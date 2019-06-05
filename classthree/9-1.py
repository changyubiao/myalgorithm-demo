#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/5 10:48
@File    : 9.py
@Author  : frank.chang@shoufuyou.com


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



if __name__ == '__main__':
    matrix = np.array([
        [1, 3, 5, 6],
        [2, 5, 7, 9],
        [4, 6, 8, 10],
    ])

    target = 7
    ret = find_targe(matrix, target)
    print(f"ret:{ret}")
    pass
