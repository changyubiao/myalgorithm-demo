#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/1 23:46
@File    : 6.py
@Author  : frank.chang@shoufuyou.com


6 旋转正方形矩阵
【 题目】 给定一个整型正方形矩阵matrix， 请把该矩阵调整成
顺时针旋转90度的样子。
【 要求】 额外空间复杂度为O(1)。



要求 是矩形 才可以的哦.


matrix:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
===>
matrix:
[[7 4 1]
 [8 5 2]
 [9 6 3]]



matrix:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
===>
matrix:
[[13  9  5  1]
 [14 10  6  2]
 [15 11  7  3]
 [16 12  8  4]]




"""

import numpy as np


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_one(self):
        self.x += 1
        self.y += 1

    def sub_one(self):
        self.x -= 1
        self.y -= 1


def test_one():
    matrix = np.arange(1, 10).reshape((3, 3))

    print(f"\nmatrix:\n{matrix}")


def test_two():
    matrix = np.arange(1, 17).reshape((4, 4))

    print(f"\nmatrix:\n{matrix}")


def rotate_edge_01(m, point_a, point_b):
    """
     对于 四个点 的情况
    :param m: matrix
    :param point_a:   两个点a
    :param point_b:   两个点b
    :return:
    """

    a_r, a_c = point_a.x, point_a.y
    b_r, b_c = point_b.x, point_b.y

    tmp = m[a_r][a_c]
    m[a_r][a_c] = m[b_r][a_c]
    m[b_r][a_c] = m[b_r][b_c]
    m[b_r][b_c] = m[a_r][b_c]
    m[a_r][b_c] = tmp

    pass


def rotate_edge(m, point_a, point_b):
    """
    旋转边  ,交换 边上 的点 .


    A     B

    C     D

    这里 需要传入  point A ,  point D

    :param m: matrix
    :param point_a:   两个点a
    :param point_b:   两个点b
    :return:


    tmp = m[a_r][a_c+1]
    m[a_r][a_c + 1] = m[b_r-1][a_c]
    m[b_r - 1][a_c] = m[b_r][b_c-1]

    m[b_r][b_c - 1] = m[a_r+1][b_c]
    m[a_r + 1][b_c] = tmp


    """
    times = point_b.x - point_a.x

    a_r, a_c = point_a.x, point_a.y

    b_r, b_c = point_b.x, point_b.y

    for i in range(0, times):
        tmp = m[a_r][a_c + i]
        m[a_r][a_c + i] = m[b_r - i][a_c]
        m[b_r - i][a_c] = m[b_r][b_c - i]

        m[b_r][b_c - i] = m[a_r + i][b_c]
        m[a_r + i][b_c] = tmp


def rotate_matrix(matrix):
    """
    旋转 矩阵
    :param matrix:
    :return:
    """
    row, column = matrix.shape
    b_r, b_c = row - 1, column - 1

    A = Point(0, 0)
    B = Point(b_r, b_c)
    while A.x < B.x:
        rotate_edge(matrix, A, B)
        A.add_one()
        B.sub_one()


def test_ege():
    matrix = np.arange(1, 17).reshape((4, 4))
    print(f"\nmatrix:\n{matrix}")

    A = Point(0, 0)
    B = Point(3, 3)

    rotate_edge(matrix, A, B)
    print(f"\nmatrix:\n{matrix}")


if __name__ == '__main__':

    matrix = np.arange(1, 17).reshape((4, 4))
    print(f"\nmatrix:\n{matrix}")
    rotate_matrix(matrix)

    print(f"\nmatrix:\n{matrix}")

