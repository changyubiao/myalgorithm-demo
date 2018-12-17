#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 14:48
@File    : 1.py
@Author  : frank.chang@shoufuyou.com


用数组结构  实现大小固定的队列和栈


1.实现 栈结构

2.实现 队列结构



"""


class ArrayToStack:

    def __init__(self, init_size):
        if init_size < 0:
            raise ValueError("The init size is less than 0")

        self.arr = [None] * init_size

        # size 表示栈的容量，同时表示 将要 插入位置的index.
        self.size = 0

    def peek(self):
        if self.size == 0:
            return
        return self.arr[self.size - 1]

    def push(self, item):
        """

        :param item:
        :return:
        """

        if self.size == len(self.arr):
            raise IndexError("The stack is full")

        # 入栈
        self.arr[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("The stack is empty")

        self.size -= 1
        return self.arr[self.size]


class ArrayQueue:
    """


    end  做为入队列的索引 ， 当end 达到 最大长度 的时候， 返回 0 位置，循环这样进行

    start 做为出队列的索引，  当 start  达到 最大长度 的时候， 返回 0 位置，循环这样进行


    put(self, item)  入队列

    get     出队列

    peek   返回队列 首元素

    is_empty  判断队列 是否为空的， True , False

    """

    def __init__(self, init_size):
        if init_size < 0:
            raise ValueError("The init size is less than 0")

        self.end = 0
        self.start = 0

        self.arr = [None] * init_size
        # 队列 当前 size
        self.size = 0

    def put(self, item):
        """
        删除并返回队首的元素。如果队列为空则会抛异常.
        :param item:
        :return:
        """

        if self.size == len(self.arr):
            raise IndexError("The queue is full")

        self.size += 1
        self.arr[self.end] = item

        self.end = 0 if self.end == self.length - 1 else self.end + 1

    def is_empty(self):
        return self.size == 0

    @property
    def length(self):
        return len(self.arr)

    def get(self):
        """
        删除并返回队首的元素。如果队列为空则会抛异常。

        Remove and return an item from the queue.

        :return:
        """

        if self.size == 0:
            raise IndexError("The stack is empty")

        # 这里要把队列的长度减1
        self.size -= 1
        tmp = self.start

        self.start = 0 if self.start == self.length - 1 else self.start + 1

        return self.arr[tmp]

    def peek(self):
        """
        返回队列 首 的元素

        :return:
        """
        if self.size == 0:
            raise IndexError("The queue is empty")

        return self.arr[self.start]


def test_stack():
    stack = ArrayToStack(5)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()




def  test_quque():
    queue = ArrayQueue(4)

    queue.put(1)
    queue.put(2)
    queue.put(3)

    queue.get()
    print(queue.peek())
    queue.put(4)

    print(queue.peek())

    # while not queue.is_empty():
    #     print(queue.get())


if __name__ == '__main__':
    pass

    queue = ArrayQueue(4)

    queue.put(1)
    queue.put(2)
    queue.put(3)

    queue.get()
    print(queue.peek())
    queue.put(4)

    print(queue.peek())

    # while not queue.is_empty():
    #     print(queue.get())


    # queue.put(1)