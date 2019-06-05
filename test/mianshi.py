#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/28 15:25
@File    : mianshi.py
@Author  : frank.chang@shoufuyou.com
"""


from operator import attrgetter


def multiple_of_three_data(data):
    """

    :param data:iterable
    :return: filter
    """

    return filter(lambda x: x % 3 == 0, data)


def sort_and_distinct(data):
    """

    :param data:  list
    :return: list
    """
    data = list(set(data))
    data.sort()
    return data


def sort_by_amount(data):
    d = sorted(data, key=lambda x: attrgetter('amount'))
    return d


def calc(operator, x, y):
    operator_mapping = {
        'multiply': '*',
        'divide': '/',

        'add': '+',
        'substract': '-'
    }

    expression = str(x) + operator_mapping[operator] + str(y)
    return eval(expression)


if __name__ == '__main__':
    # data = range(10)
    # l = multiple_of_three_data(data)
    # print(list(l))

    print(calc('add', 3, 4))
    print(calc('multiply', 3, 4))
    print(calc('divide', 3, 4))
    print(calc('substract', 3, 4))
    pass
