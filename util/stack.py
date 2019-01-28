#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 16:07
@File    : stack.py
@Author  : frank.chang@shoufuyou.com
"""


class Stack:
    """模拟栈
    Stack()    建立一个空的栈对象

    push()     把一个元素添加到栈的最顶层
    pop()      删除栈最顶层的元素，并返回这个元素
    peek()     返回最顶层的元素，并不删除它
    is_empty()  判断栈是否为空
    size()     返回栈中元素的个数

    """

    def __init__(self):
        self.items = []
        self._size = len(self.items)

    def print_stack(self):

        for item in self.items:
            print(item, end=' ')

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)
        self._size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("stack is empty now.")

        self._size -= 1
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    @property
    def size(self):
        return self._size


if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    # stack.push(10)
    # stack.push(10)
    # stack.push(10)
    # stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)

    print(stack.size)

    print(stack.print_stack())
    # stack.pop()
    # stack.pop()
