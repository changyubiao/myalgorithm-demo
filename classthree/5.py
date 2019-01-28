#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/1 13:21
@File    : 5.py
@Author  : frank.chang@shoufuyou.com


转圈打印矩阵
【 题目5 】 给定一个整型矩阵matrix， 请按照转圈的方式打印它。
例如： 1   2   3    4
      5   6   7    8
      9   10  11   12
     13   14  15   16


array=[
     [ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]
]

打印结果为： 1， 2， 3， 4， 8， 12， 16， 15， 14， 13， 9，5， 6， 7， 11， 10

【要求】 额外空间复杂度为O(1)



按顺时针方向 每一圈 进行遍历,之后  , 在内圈 也这样遍历, 最后结果就是 按照 顺时针的方向 进行遍历.


 ----- |
"""

import numpy as np


class Point:
    """ Point

    定义一个辅助的 数据结构 point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"

    __repr__ = __str__


def print_edge_old(matrix, a, b):
    """
    first version
    :param matrix:  矩阵
    :param a: point  a
    :param b: point  b
    :return:


    """

    X, Y = a.x, a.y

    m, n = b.x, b.y

    if X == m:
        for i in range(Y, n + 1):
            # 水平 方向
            print(matrix[X][i], end=' ')
    elif Y == n:
        for i in range(X, m + 1):
            # 竖直 方向
            print(matrix[i][Y], end=' ')
    else:
        # 构成一个矩形
        while a.y < b.y and Y < b.y:
            print(matrix[a.x][Y], end=' ')
            Y += 1

        while a.x < b.x and X < b.x:
            print(matrix[X][b.y], end=' ')
            X += 1

        # 重置 y 坐标
        Y = n
        while a.y < b.y and Y > a.y:
            print(matrix[b.x][Y], end=' ')
            Y -= 1

        X = m
        while a.x < b.x and X > a.x:
            print(matrix[X][a.y], end=' ')
            X -= 1


def print_edge(matrix, a, b):
    """
    打印 最外围的 一圈 的边
    :param matrix:  矩阵
    :param a: point  a
    :param b: point  b
    :return:



    """

    cur_index = a.x
    cur_column = a.y

    if a.x == b.x:
        for i in range(a.y, b.y + 1):
            # 水平 方向 [a.y,b.y] 进行打印
            print(matrix[a.x][i], end=' ')
    elif a.y == b.y:
        for i in range(a.x, b.x + 1):
            # 竖直 方向
            print(matrix[i][a.y], end=' ')
    else:
        # 构成一个矩形 的情况

        #  ---  从左向右
        while cur_column != b.y:
            print(matrix[a.x][cur_column], end=' ')
            cur_column += 1

        # | 从上到下
        while cur_index != b.x:
            print(matrix[cur_index][b.y], end=' ')
            cur_index += 1

        # --- 从右向左
        while cur_column != a.y:
            print(matrix[b.x][cur_column], end=' ')
            cur_column -= 1

        # | 从下向上
        while cur_index != a.x:
            print(matrix[cur_index][a.y], end=' ')
            cur_index -= 1


def print_matrix(matrix, a, b):
    """


    :param matirx:
    :param a: point
    :param b: point
    :return:
    """

    while a.x <= b.x and a.y <= b.y:
        print_edge(matrix, a, b)

        a.x += 1
        a.y += 1
        b.x -= 1
        b.y -= 1


def test_one():
    matrix = np.arange(1, 16).reshape((5, 3))

    A = Point(0, 0)
    B = Point(4, 2)
    print_matrix(matrix, A, B)

    print(f"\nmatrix:\n{matrix}")


def test_two():
    matrix = np.arange(1, 17).reshape((4, 4))

    A = Point(0, 0)
    B = Point(3, 3)
    print_matrix(matrix, A, B)

    print(f"\nmatrix:\n{matrix}")


if __name__ == '__main__':
    test_one()

    test_two()

    pass
