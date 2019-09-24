#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@User    : frank 
@Time    : 2019/7/24 22:22
@File    : queue.py
@Email  : frank.chang@xinyongfei.cn
"""


class Queue:
    """
    Queue()    建立一个空的队列对象
    enqueue()   入队列
    dequeue()    出队列
    peek()     返回 队列 对首的元素，并不删除它
    is_empty()  判断队列是否为空
    size()     返回队列中元素的个数
    """

    def __init__(self):
        self.items = []
        self._size = len(self.items)

    def enqueue(self, item):
        """
        入队列
        :param item:
        :return:
        """
        self.items.append(item)
        self._size += 1

    def dequeue(self):
        """
        出队列
        :return:
        """
        if self.size == 0:
            raise IndexError("queue is empty now.")

        item = self.items.pop(0)

        self._size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise IndexError("queue is empty now.")

        return self.items[0]

    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return self._size



if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.size)

    print(q.dequeue())
    print(q.dequeue())

    print(q.dequeue())
    print(q.dequeue())

    print(q.size)

    # q.dequeue()

    pass
