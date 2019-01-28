#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/30 10:37
@File    : test_getiem.py
@Author  : frank.chang@shoufuyou.com


refer :
  https://blog.csdn.net/weixin_42557907/article/details/81589574
"""


class Tag1:
    """


    tag = Tag()
    tag['name']  --->   __getitem__

    """

    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        print(f'__getitem__({item})  is  called.')
        return 2


class Tag_2:
    """


    tag = Tag()

    tag['name']  --->   __getitem__

    tag['name'] ='frank'   ----> __setitem__

    """

    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        print(f'__getitem__({item})  is  called.')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print("__setitem__:Set %s Value %s" % (key, value))

        self.__dict__[key] = value


class Tag:
    """


    tag = Tag()

    tag['name']  --->   __getitem__

    tag['name'] ='frank'   ----> __setitem__

    del tag['name']  ---->  __delitem__
    """

    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        print(f'__getitem__({item}) is  called.')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print(f"__setitem__:Set {key},Value {value}")

        self.__dict__[key] = value

    def __delitem__(self, key):
        print(f"__delitem__({key}) is called")
        del self.__dict__[key]


def test_tag():
    tag = Tag()

    # __getitem__ is called
    print(tag['name'])  # 2
    print(tag['frank'])  # 2
    print(tag['laoda'])  # 2


def test_tag2():
    tag = Tag()

    tag['name'] = 'frank'
    tag['laoda'] = 'liuxiaolu'
    print(tag['laoda'])
    print('frank')


if __name__ == '__main__':
    tag = Tag()

    #  __setitem__ 被调用
    tag['name'] = 'frank'
    tag['laoda'] = 'liuxiaolu'
    tag['laoer'] = 'lile'
    tag['laosan'] = 'weiliang'

    # __getitem__  被调用
    print(tag['laosan'])

    #  __delitem__  被调用
    del tag['laosan']

    try:
        print(tag['laosan'])
    except KeyError:
        print('key error occurred.')



import requests

from urllib.parse import  urlparse