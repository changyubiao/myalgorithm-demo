#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/6 16:08
@File    : 13.py
@Author  : frank.chang@shoufuyou.com



13  复制含有随机指针节点的链表
【题目】 一种特殊的链表节点类描述如下：


class Node:

    def __init__(self, data):
        self.value = data

        # 指向下一个结点
        self.next = None

        # 随机的一个指针
        self.rand = None






Node类中的value是节点值，next指针和正常单链表中next指针的意义一 样，都指向下一个节点，
rand指针是Node类中新增的指针，这个指针可 能指向链表中的任意一个节点，也可能指向null。

给定一个由 Node节点类型组成的无环单链表的头节点head，



请实现一个函数完成 这个链表中所有结构的复制， 并返回复制的新链表的头节点。




进阶：
不使用额外的数据结构，只用有限几个变量，且在时间复杂度为 O(N)内 ,完成原问题要实现的函数。







1  ---->  2  --->  3 ---> null


1.rand  -->3
2.rand ---> 1
3.rand  ----> null






还有一种比较复杂 不使用哈希表, 来做这个事情.

时间 复杂度 . O(N) 空间复杂度 O(N)


第一步
1 --->1' ---->    2  -----> 2' ------>  3 ----->   3'


第二步 :
更改rand结点

 1' 的rand  就是1 的rand 的next 就是 1'rand 应该连接的位置


第三步  :

想办法 分离 这个长的链表.












"""


class Node:

    def __init__(self, data):
        self.value = data

        # 指向下一个结点
        self.next = None

        # 随机的一个指针
        self.rand = None

    # def __repr__(self):
    #     return f'Node({self.value})'
    #
    # __str__ = __repr__


def print_node(node):
    """
    打印 链表
    :param node:
    :return:
    """

    # print("Linked List: ", end='')

    print("Linked List: ")
    p = node
    while p:
        print(f"{p.value},{id(p)}")
        p = p.next

    print(" ")


def print_rand_info(head):
    """
    打印每个结点的rand 信息
    :param head:
    :return:
    """
    p = head

    while p:
        print()
        print(f"cur_node: Node({p.value},{ id(p.rand)})", end=' ')
        # print(f'{p.rand}', end=' ')

        p = p.next

    print("")

def copy_listwith_rand(head):
    """

    :param head:
    :return:
    """

    #  结点 和copy 结点 之间的映射
    mapping = dict()

    p = head
    # 先把 结点 和copy结点 建立一个映射
    while p is not None:
        mapping.update({p: Node(p.value)})
        p = p.next

    # copy 完成 后
    p = head

    # 重新遍历链表
    while p is not None:
        # print(f"handle  cur_node: Node({p.value})")
        # 处理 next 结点
        if p.next is None:
            mapping[p].next = None
        else:
            mapping[p].next = mapping[p.next]

        # 处理rand 结点
        if p.rand is None:
            mapping[p].rand = None
        else:
            mapping[p].rand = mapping[p.rand]

        p = p.next

    # print('--------end  copy -----')
    # copy 后的 头结点
    return mapping[head]


def test_copy():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.rand = head.next.next.next.next.next  # 1 -> 6
    head.next.rand = head.next.next.next.next.next  # 2 -> 6
    head.next.next.rand = head.next.next.next.next  # 3 -> 5
    head.next.next.next.rand = head.next.next  # 4 -> 3
    head.next.next.next.next.rand = None  # 5 -> null
    head.next.next.next.next.next.rand = head.next.next.next  # 6 -> 4

    print_node(head)
    print_rand_info(head)

    # copy node
    copy_head = copy_listwith_rand(head)

    print('---'*20)
    print_node(copy_head)
    print_rand_info(copy_head)


def test_copy2():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node1.rand = node3

    node2.next = node3
    node2.rand = node1

    node3.rand = None

    print_node(node1)

    print_rand_info(node1)

    copy_head = copy_listwith_rand(node1)
    print_node(copy_head)

    pass


if __name__ == '__main__':
    test_copy()
    print('frank')
    pass
