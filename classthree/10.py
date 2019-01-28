#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/9 14:15
@File    : 10.py
@Author  : frank.chang@shoufuyou.com



打印两个有序链表的公共部分
【 题目】 给定两个有序链表的头指针head1和head2， 打印两个
链表的公共部分。






"""


class Node:
    """
    链表 node 的 定义
    """

    def __init__(self, data):
        self.value = data
        self.next = None


def print_node(node):
    """
    打印 链表
    :param node:
    :return:
    """
    p = node
    while p:
        print(f"{p.value}", end=' ')
        p = p.next


def print_common_part(head1, head2):
    """
    打印两个有序链表的 公共部分
    :param head1:
    :param head2:
    :return:
    """

    p1 = head1
    p2 = head2

    if head1 is None or head2 is None:
        return

    while p1 and p2:
        if p1.value > p2.value:
            p2 = p2.next
        elif p1.value < p2.value:
            p1 = p1.next
        else:
            print(f"{p1.value}", end=' ')
            p1 = p1.next
            p2 = p2.next


def test_print_common_part():
    node0 = Node(1)
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(7)
    node4 = Node(10)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print('\n----------------node0')
    print_node(node0)

    second_node0 = Node(4)
    second_node1 = Node(7)
    second_node2 = Node(8)
    second_node3 = Node(10)
    second_node4 = Node(13)

    second_node0.next = second_node1
    second_node1.next = second_node2
    second_node2.next = second_node3
    second_node3.next = second_node4

    print('\n----------------secondnode0')
    print_node(second_node0)

    print('\n----------------common part')
    print_common_part(node0, second_node0)


if __name__ == '__main__':
    test_print_common_part()
    pass
