#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/26 19:44
@File    : 14.py
@Author  : frank.chang@shoufuyou.com



题目十四   两个单链表相交的一系列问题


【题目】 在本题中，单链表可能有环，也可能无环。给定两个单链表的头节点 head1和head2，这两个链表可能相交，也可能
不相交。


请实现一个函数,   如果两个链表相交，请返回相交的第一个节点；
                如果不相交，返回null 即可 ;



要求：如果链表1的长度为N，链表2的长度为M，时间复杂度请达到 O(N+M)，额外空间复杂度请达到O(1)。











"""

import random


class Node:

    def __init__(self, data):
        self.value = data

        # 指向下一个结点
        self.next = None

        # 随机的一个指针
        self.rand = None


def create_linknode(array):
    """
    辅助 生成Node结构   , 返回头结点
    create linknode   返回 第一个 node
    :param array:  [1,2,3,4,5]
    :return: head
    """

    from itertools import islice
    nodes = [Node(num) for num in array]

    max_index = len(nodes) - 1

    for idx, node in enumerate(islice(nodes, 0, max_index)):
        node.next = nodes[idx + 1]

    head = nodes[0]
    return head


def print_node(node):
    """
    打印 链表
    :param node:
    :return:
    """

    print("Linked List: ", end='')
    p = node
    while p:
        print(f"{p.value}", end=' ')
        p = p.next

    print("")


if __name__ == '__main__':
    array = list(range(10))

    random.shuffle(array)

    print(f"array:{array}")

    head = create_linknode(list(range(10)))

    print_node(head)
    pass


    s1 = set([1,2,3])
    s2 = set([4,5,6])


