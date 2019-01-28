#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/12 00:44
@File    : reverse_word.py
@Author  : frank.chang@shoufuyou.com


LeetCode | Reverse Words in a String


题目：
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".



"""


def reverse_words(string):
    """
    逆序 单词
    :param string:
    :return:
    """
    words = string.split()
    reverse_list = list(reversed(words))
    ret = ' '.join(reverse_list)
    return ret


if __name__ == '__main__':
    s = "the sky is blue"

    ret = reverse_words(s)

    print(f"ret: {ret}")

    pass
