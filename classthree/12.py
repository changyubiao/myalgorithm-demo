#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/22 16:17
@File    : 12.py
@Author  : frank.chang@shoufuyou.com


类似 荷兰国旗问题.






将单向链表按某值划分成左边小、中间相等、右边大的形式
【题目】 给定一个单向链表的头节点head，节点的值类型是整型，再给定一个
整 数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于 pivot
的节点，中间部分都是值等于pivot的节点，右部分都是值大于 pivot的节点。
除这个要求外，对调整后的节点顺序没有更多的要求。 例如：链表9->0->4->5-
>1，pivot=3。 调整后链表可以是1->0->4->9->5，也可以是0->1->9->5->4。总
之，满 足左部分都是小于3的节点，中间部分都是等于3的节点（本例中这个部
分为空），右部分都是大于3的节点即可。对某部分内部的节点顺序不做 要求。












进阶： 在原问题的要求之上再增加如下两个要求。
在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左 到右的
顺序与原链表中节点的先后次序一致。

例如：链表9->0->4->5->1，pivot=3。
调整后的链表是0->1->9->4->5。
在满足原问题要求的同时，左部分节点从左到
右为0、1。在原链表中也 是先出现0，后出现1；
中间部分在本例中为空，不再讨论；
右部分节点 从左到右为9、4、5。在原链表中也是先出现9，然后出现4，
最后出现5。



要求:
如果链表长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。

"""

import random


def partition(array, left, right, num):
    """
    返回 一个元祖
    荷兰国旗问题
    :param array:  []
    :param left: left
    :param right: right
    :param num:
    :return: 返回一个 num 相同位置的 index ,左边 index ,右边 index
    """
    less = left - 1
    more = right + 1
    cur = left

    while cur < more:
        if array[cur] < num:
            array[less + 1], array[cur] = array[cur], array[less + 1]
            cur = cur + 1
            less = less + 1
        elif array[cur] > num:
            array[more - 1], array[cur] = array[cur], array[more - 1]
            more = more - 1
        else:  # ==num
            cur = cur + 1

    return less + 1, more - 1


class Node:
    """
    链表 node 的 定义
    """

    def __init__(self, data):
        self.value = data
        self.next = None


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


def partition2(head, pivot):
    """

    :param head:
    :param pivot:  中心点
    :return:  head
    """

    cur = head

    less, more, equal = None, None, None

    while cur:

        if cur.value < pivot:
            # less
            less = Node(cur.value)
            break

    cur = head

    while cur:
        if cur.value > pivot:
            # more

            more = Node(cur.node)
            break

    cur = head

    while cur:
        if cur.value == pivot:
            # equal
            equal = Node(cur.value)


    if  more  and  less  and  equal:
        pass






def fun():pass



if __name__ == '__main__':
    # array = list(range(10))
    # random.shuffle(array)

    array = [9, 0, 4, 5, 1]

    node = create_linknode(array)

    print(node)

    print_node(node)

    # right = len(array) - 1
    # print(array)
    #
    # partition(array, 0, right, 6)

    # print(array)

    pass
