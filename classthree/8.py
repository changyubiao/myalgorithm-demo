#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/5 10:48
@File    : print_matrix_zig_zag.py
@Author  : frank.chang@shoufuyou.com




之” 字形打印矩阵
【 题目】 给定一个矩阵matrix， 按照“之” 字形的方式打印这
个矩阵， 例如： 1 2 3 4 5 6 7 8 9 10 11 12
“之” 字形打印的结果为： 1， 2， 5， 9， 6， 3， 4， 7， 10， 11，
8， 12
【 要求】 额外空间复杂度为O(1)



"""

import numpy as np


def print_line(matrix, a_r, a_c, b_r, b_c, reverse=True):
    """


    A (a_r,a_c)
    B (b_r,b_c)

    :param matrix:
    :param a_r:
    :param a_c:
    :param b_r:
    :param b_c:
    :param reverse:
    :return:
    """
    if reverse:
        while a_r != b_r + 1:
            # 从 右上  -->  左下 打印
            print(matrix[a_r][a_c], end=' ')
            a_r += 1
            a_c -= 1
    else:
        while b_c != a_c + 1:
            # 从左下, --->  右上 打印
            print(matrix[b_r][b_c], end=' ')
            b_r -= 1
            b_c += 1

    # print('-------' * 5)


def _print_matrix_zig_zag(matrix):
    a_r, a_c = 0, 0

    b_r, b_c = 0, 0

    #
    row, column = matrix.shape

    print(f"row:{row},column:{column}")

    from_up = True
    while True:
        # print_line(matrix, a_r, a_c, b_r, b_c,from_up)
        print('----')
        if (a_r, a_c) == (row - 1, column - 1):
            break

        # A 向 右走, 之后 向下走
        a_r = a_r + 1 if a_c == column - 1 else a_r
        a_c = a_c if a_c == column - 1 else a_c + 1

        # B 向下走,之后 向右走
        b_c = b_c + 1 if b_r == row - 1 else b_c
        b_r = b_r if b_r == row - 1 else b_r + 1

        A = (a_r, a_c)
        B = (b_r, b_c)

        from_up = not from_up

        # print(f"A:{A},B:{B}")

    # print_line()
    print()


def print_matrix_zig_zag(matrix):
    # A 点
    a_r, a_c = 0, 0

    # B 点
    b_r, b_c = 0, 0

    row, column = matrix.shape
    print(f"row:{row},column:{column}")
    up = True
    while True:
        print('----')
        print_line(matrix, a_r, a_c, b_r, b_c, reverse=up)
        # 走到了 最后一个位置 , 退出条件
        if (a_r, a_c) == (row - 1, column - 1):
            break

        # A 向右走, 之后向下走
        a_r = a_r + 1 if a_c == column - 1 else a_r
        a_c = a_c if a_c == column - 1 else a_c + 1

        # B 向下走,之后 向右走
        b_c = b_c + 1 if b_r == row - 1 else b_c
        b_r = b_r if b_r == row - 1 else b_r + 1

        up = not up


def test_print_matrix_zig(matrix):
    # A 点
    a_r, a_c = 0, 0

    # B 点
    b_r, b_c = 0, 0

    row, column = matrix.shape

    #  矩形对应的 index 下标
    row_index = row - 1
    column_index = column - 1

    while True:
        print('-------------')

        # A 向 右走, 之后 向下走
        a_r = a_r + 1 if a_c == column_index else a_r
        a_c = a_c if a_c == column_index else a_c + 1

        # B 向下走,之后 向右走
        b_c = b_c + 1 if b_r == row_index else b_c
        b_r = b_r if b_r == row_index else b_r + 1

        A = (a_r, a_c)
        B = (b_r, b_c)

        print(f"A:{A},B:{B}")
        if A == B:
            print('A==B  break')
            break


def test_line():
    matrix = np.arange(0, 24).reshape((4, 6))

    print_line(matrix, 0, 3, 3, 0, reverse=True)

    print()
    print_line(matrix, 0, 3, 3, 0, reverse=False)

    print(f"\nmatrix:\n{matrix}")


if __name__ == '__main__':
    matrix = np.arange(0, 24).reshape((4, 6))

    print_matrix_zig_zag(matrix)

    print(f"\nmatrix:\n{matrix}")
    pass
