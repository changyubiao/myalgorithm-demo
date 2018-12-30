#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/18 18:19
@File    : frank1.py
@Author  : frank.chang@shoufuyou.com
"""

import random


# left even, right odd
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# odd = even = -1
# length = len(data)
#
# def is_even(item):
#     return not bool(item % 2)
#
# def swap(d, left, right):
#     d[left], d[right] = d[right], d[left]
#
# def f(odd, even):
#     for i in range(length):
#         odd += 1
#         # if data[i] is even
#         if is_even(data[i]):
#             even += 1
#             tmp = i
#             while tmp > even:
#                 swap(data, tmp-1, tmp)
#                 tmp -= 1
#                 print(f'==={data}===')
#         print(data)
# print(data)
# print(f'even={even+1}, odd={odd-even}')

# def find_odd(array):
#     #  寻找偶数
#     for i, num in enumerate(array):
#         if num % 2 == 0:
#             return i
#
#     return -1







def partition(array, L, R):
    # odd = L - 1

    even = L - 1

    cur = L+1

    # pos = find_odd(array)
    # if pos == -1:
    #     return
    #
    # array[0], array[pos] = array[pos], array[0]


    odd = L

    while cur < R:

        if cur % 2 == 0:

            # odd += 1

            cur += 1

        else:  # 奇数
            even  = cur

            # 移动数据

            #
            cur += 1

if __name__ == '__main__':
    data = list(range(10))
    random.shuffle(data)
    print(data)

    # data = [3, 1, 9, 5, 0, 6, 7, 8, 4, 2]

    # l = 0
    # r = len(mylist) - 1
    # partition(array=mylist, L=l, R=l)
    #
    # print(mylist)
    pass

    # data = [1, 2, 3, 4, 5, 6, 7, 8]
    # odd = even = -1
    # length = len(data)


    def is_even(item):
        return not bool(item % 2)


    def swap(d, left, right):
        d[left], d[right] = d[right], d[left]


    def f(data,odd, even):
        length = len(data)

        for i in range(length):
            odd += 1
            # if data[i] is even
            if is_even(data[i]):
                even += 1
                tmp = i
                while tmp > even:
                    swap(data, tmp - 1, tmp)
                    tmp -= 1
                    print(f'==={data}===')
            print(data)




    f(data,-1,-1)

    print(data)

    print(f'even={even+1}, odd={odd-even}')
