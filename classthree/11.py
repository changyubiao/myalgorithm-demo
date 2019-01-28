#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/6 16:08
@File    : 11.py
@Author  : frank.chang@shoufuyou.com



判断一个链表是否为回文结构
【 题目】 给定一个链表的头节点head， 请判断该链表是否为回文结构。


例如：     1->2->1，   返回true。 1->2->2->1， 返回true。


          15->6->15， 返回true。 1->2->3，    返回false。


进阶： 如果链表长度为N， 时间复杂度达到O(N)， 额外空间复杂度达到O(1)。

"""

from util.stack import Stack


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

    print("Linked List: ", end='')
    p = node
    while p:
        print(f"{p.value}", end=' ')
        p = p.next

    print("")


def is_huiwen(head: Node):
    """
    用辅助栈来实现


    用辅助空间 ,加上栈结构来实现
    :param head:
    :return:
    """
    stack = Stack()
    p = head
    while p:
        stack.push(p.value)
        p = p.next

    p = head
    flag = True
    while p:
        left = p.value
        right = stack.pop()

        if left != right:
            flag = False
            break
        p = p.next

    return flag


def is_palindrome2(head: Node):
    """
    o/2   用两个指针来控制,一个快指针, 一个正常的速度的指针.
    :param head:
    :return: true or  false
    """
    flag = True
    if not head:
        return True

    p = head
    fast = head
    stack = Stack()

    while p and fast and fast.next and fast.next.next:
        p = p.next
        fast = fast.next.next

    # 奇数的情况 node 个数, 0 1 ...  6
    if not fast.next:
        print("奇数的情况node个数, 0 1 ..  6 ")
        cur = p.next
        while cur:
            stack.push(cur.value)
            cur = cur.next
    else:
        # 偶数的情况
        # fast.next 不为空的情况:
        print("偶数的情况node个数, 0 1 ..  5")
        cur = p.next
        while cur:
            stack.push(cur.value)
            cur = cur.next

    while not stack.is_empty():
        front = head.value
        last = stack.pop()

        if front != last:
            flag = False
            break
        head = head.next
    return flag


def test_is_huiwen():
    node0 = Node(1)
    node1 = Node(3)
    node2 = Node(4)
    node21 = Node(4)
    node3 = Node(3)
    node4 = Node(1)
    node0.next = node1
    node1.next = node2
    node2.next = node21
    node21.next = node3
    node3.next = node4

    # flag = is_huiwen(node0)

    # print(f'flag  :{flag}')

    print_node(node0)


def create_linknode(array):
    """
    辅助 生成Node结构   , 返回头结点
    create linknode   返回 第一个 node
    :param array:  [1,2,3,4,5]
    :return: head
    """

    from itertools import islice
    nodes = [Node(num) for num in array]

    max_index = len(nodes)-1

    for idx, node in enumerate(islice(nodes, 0, max_index)):
        node.next = nodes[idx + 1]
        # print(node.value)

    head = nodes[0]

    return head


def test_is_palindrome2():
    node0 = Node(1)
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(3)
    node4 = Node(1)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print_node(node0)
    # flag = is_huiwen(node0)

    # print(f'flag  :{flag}')

    ret = is_palindrome2(node0)

    print(f"ret:{ret}")


if __name__ == '__main__':
    # is_palindrome2()
    # test_is_palindrome2()

    array = [1, 2,3,2,1]
    node0 = head = create_linknode(array)

    print_node(head)
    ret = is_palindrome2(node0)
    print(f"ret:{ret}")