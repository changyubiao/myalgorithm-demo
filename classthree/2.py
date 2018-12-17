#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 15:13
@File    : 2.py
@Author  : frank.chang@shoufuyou.com



实现一个特殊的栈， 在实现栈的基本功能的基础上， 再实现返
回栈中最小元素的操作。get_min   返回最小值
【 要求】
1． pop、 push、 getMin操作的时间复杂度都是O(1)。
2． 设计的栈类型可以使用现成的栈结构。





维护两个栈


data  放数据       min  栈



data 正常 压栈 ,出栈,  min  栈 每一次压入最小值 ,入栈 .







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


class MyStack:

    def __init__(self):
        self.data = Stack()

        self.min = Stack()

    def pop(self):

        if self.data.is_empty():
            raise RuntimeError("stack is empty now.")

        item = self.data.pop()
        self.min.pop()
        return item

    def push(self, item):

        self.data.push(item)

        if self.min.is_empty():
            self.min.push(item)
        else:
            top = self.min.peek()
            # 每次push 最小值
            if item > top:
                # 把top 在push  一次
                self.min.push(top)
            else:
                self.min.push(item)

    def get_min(self):

        if self.data.is_empty():
            raise RuntimeError("stack is empty now.")

        return self.min.peek()


if __name__ == '__main__':
    stack = MyStack()

    stack.push(3)

    stack.get_min()

    print(stack.get_min())

    stack.push(4)
    print(stack.get_min())

    stack.push(1)
    print(stack.get_min())

    stack.push(13)

    stack.push(2)
    print(stack.get_min())
    stack.push(15)
    stack.push(10)

    print(stack.get_min())

    pass
