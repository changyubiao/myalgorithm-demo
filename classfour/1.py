#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/10 22:16
@File    : 1.py
@Author  : frank.chang@shoufuyou.com


二叉树相关练习


实现  二叉树的先序、中序、后序遍历，包括递归方式和非递归方式

"""

from util.stack import Stack


class Node:
    """
    二叉树 结点
    """

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def main():
    """
                         5
            3                           8
          2  4                       7      10
        1                          6       9 11



    三种遍历方式如下:

    5 3 2 1 4 8 7 6 10 9 11 ========pre-order ===========
    1 2 3 4 5 6 7 8 9 10 11 ========in-order  ===========
    1 2 4 3 6 7 9 11 10 8 5 ========post-order===========

    :return:
    """
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    print("\npre_order:  ")
    pre_order(head)

    pre_order_stack(head)

    # print("\nin_order: ")
    # in_order(head)
    #
    # print("\npost_order: ")
    # post_order(head)

    pass


def pre_order(head: Node):
    if head is None:
        return

    print(head.value, end=' ')
    pre_order(head.left)
    pre_order(head.right)


def in_order(head: Node):
    if head is None:
        return

    in_order(head.left)
    print("{}".format(head.value), end=' ')
    in_order(head.right)


def post_order(head: Node):
    if head is None:
        return

    post_order(head.left)
    post_order(head.right)
    print("{}".format(head.value), end=' ')


def pre_order_stack(head: Node):
    """
    非递归的实现版本. 先序遍历


    用辅助栈来实现 先序遍历 ,先压 head,之后,
    循环条件:  栈不为空

    把孩子的结点的 右边孩子有的话,压入栈中.
    如果 有左孩子的话 , 也把结点压入栈中.

    这样 之后 从栈中弹出的时候,就会先出栈的是做孩子, 之后 之后才是右孩子.
    这样就可以实现先序遍历.
    :param head:
    :return:
    """

    if head is not None:
        print("\npre_order_stack: ")
        stack = Stack()

        stack.push(head)

        while not stack.is_empty():

            head = stack.pop()
            print("{}".format(head.value), end=' ')

            # 注意这里一定要先压右孩子,后压左孩子.
            if head.right is not None:
                stack.push(head.right)

            if head.left is not None:
                stack.push(head.left)

    print("")


def in_order_stack(head: Node):
    """
    中序遍历 非递归实现     left  root  right
    中序遍历,首先呢,先要找到左边界,就是最左边的孩子, 如果不用递归实现,还是要用辅助栈来完成这个事情.


    首先有一个 循环 来 控制 如何退出:  循环条件是:  栈不为空, 或者 head 不是空的. 两者 成立一个就可以了.


    首先 如果 head 不为空,就把 head 压入 栈中, 之后 head 往左走一步,继续这样直到走到没有左孩子,开始把栈中的元素弹出.然后 打印出来.

    之后 把 弹出结点的 的 右孩子压入栈中.   继续循环.


    left  root  right

    其实意思就是 先把 左边的左子树 压入栈中, 之后弹出,开始压入 右边的 孩子,如果 右孩子没有值,  栈中 弹一个元素出来.


    当前结点 为空, 从栈中取一个元素,然后当前 结点开始向右走,
    如果当前结点 不为空, 把当前结点 压入栈中, 结点开始向左走.

    :return:
    """

    if head is not None:
        stack = Stack()
        while not stack.is_empty() or head is not None:

            if head is not None:
                stack.push(head)
                head = head.left
            else:
                # head is None,从栈中取结点,其实这个时候就是上一层结点.
                head = stack.pop()
                print("{}".format(head.value), end=' ')
                head = head.right
        print(" ")


def post_order_stack(head: Node):
    """
    后序遍历  非递归的实现


    可以借助 两个栈来实现:
    help_stack  用来存放 结点的顺序为 root  right  left


    可以借助先序遍历 思想  中 左右  --->  中右左  --->  之后借助 一个辅助栈,编程  左右中,这个就是后续遍历.
    首先把  head 入栈, 之后进入循环,只要栈不为空,
    取出栈顶元素, 压入到print_stack 中, 之后 在依次出栈就可以了.


    help_stack  的作用 和先序遍历一个意思, 只是 先 压入左孩子, 之后 压入右孩子.
    :param head:
    :return:
    """
    print_stack = Stack()
    help_stack = Stack()

    if head is not None:
        print("post_order_stack: ")

        help_stack.push(head)

        while not help_stack.is_empty():
            head = help_stack.pop()
            print_stack.push(head)

            # 先放入左边, 之后放右边的节点.
            if head.left is not None:
                help_stack.push(head.left)

            if head.right is not None:
                help_stack.push(head.right)

        # end while
        while not print_stack.is_empty():
            cur = print_stack.pop()
            print("{}".format(cur.value), end=' ')


def create_three():
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    return head


if __name__ == '__main__':

    head = create_three()



    # pre_order(head)
    # print('===================')
    # in_order(head)
    #
    # print('===================')
    # post_order(head)
    # print('===================')


    # post_order_stack(head)
    #
    # print("\npost_order: ")
    # post_order(head)
    pass
