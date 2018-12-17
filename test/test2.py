#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 09:55
@File    : test2.py
@Author  : frank.chang@shoufuyou.com


info = [

    {"name": "laoda", "age": 12, "height": "175"},
    {"name": "laoda", "age": 22, "height": "180"},
    {"name": "laoda", "age": 42, "height": "160"},
]


"""

from operator import itemgetter, attrgetter


class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return '%s(name:%s,age:%s,score:%s)' % (self.__class__.__name__, self.name, self.age, self.score)

    __repr__ = __str__



if __name__ == '__main__':
    std1 = Student("A", 11, 23)
    std2 = Student("B", 13, 10)
    std3 = Student("C", 16, 15)
    std4 = Student("D", 34, 4)

    students = [std1, std2, std3, std4]

    students.sort(key=lambda student: student.score, reverse=True)

    # print(students)
    for item in students:
        print(item)

    print(sorted(students, key=attrgetter('age'), reverse=True))
