#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 11:06
@File    : test3.py
@Author  : frank.chang@shoufuyou.com



python 堆和优先队列的使用   https://blog.csdn.net/liu2012huan/article/details/53264162

https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
"""
import heapq
from operator import itemgetter, attrgetter
from queue import PriorityQueue


class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return '%s(name:%s,age:%s,score:%s)' % (self.__class__.__name__, self.name, self.age, self.score)

    __repr__ = __str__

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score


class __PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# PriorityQueue


if __name__ == '__main__111':
    std1 = Student("A", 11, 23)
    std2 = Student("B", 13, 10)
    std3 = Student("C", 16, 15)
    std4 = Student("D", 34, 4)

    students = [std1, std2, std3, std4]

    q = PriorityQueue()

    q.put(std1)
    q.put(std2)
    q.put(std3)
    q.put(std4)

    while not q.empty():
        print(q.get())

if __name__ == '__main__':

    # q = PriorityQueue(1,'frank')

    q = PriorityQueue()
    q.put(10)
    q.put(67)
    q.put(1)
    q.put(30)
    q.put(14)

    while not q.empty():
        print(q.get())
