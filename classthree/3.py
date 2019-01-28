#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/16 15:16
@File    : 3.py
@Author  : frank.chang@shoufuyou.com


如何仅用队列结构     实现   栈结构？   用两个栈来实现


如何仅用栈结构      实现    队列结构？




"""
from queue import Queue
from util.stack import Stack


class MyStack:
    """
    用两个 队列结构  实现栈结构
    """

    def __init__(self):
        self.data = Queue()
        self.help = Queue()

    def push(self, item):
        """
        入栈
        :param item:
        :return:
        """

        self.data.put(item)

    def pop(self):
        """
        出栈
        :return:
        """

        if self.data.empty():
            raise RuntimeError("Stack is empty!")

        while self.data.qsize() > 1:
            item = self.data.get()
            self.help.put(item)

        # 出栈元素
        ret = self.data.get()

        # 交换两个引用
        self.data, self.help = self.help, self.data
        return ret

    def peek(self):
        """
        取得栈顶元素,不弹出栈
        :return:
        """

        if self.data.empty():
            raise RuntimeError("Stack is empty!")

        while self.data.qsize() > 1:
            item = self.data.get()
            self.help.put(item)

        ret = self.data.get()

        self.data.put(ret)

        return ret


class MyQueue:
    """
    用两个栈结构 ,来实现队列结构


    每次 只从 help  取数据

    每次只从 push_stack  进入 数据.



    """

    def __init__(self):
        self.push_stack = Stack()
        self.help = Stack()
        # 记录当前队列的大小
        self._size = 0

    def put(self, item):
        """
        入队列


        每次 入队列 一定要进 push_stack ,


        :param item:
        :return:
        """
        self.push_stack.push(item)
        self._size += 1

    def get(self):
        """
        出队列
        每次 出队列 从  help 取出数据.
        :return:


        # if self.help.is_empty():
        #
        #     while self.push_stack.size > 1:
        #         item = self.push_stack.pop()
        #         self.help.push(item=item)
        #
        #     return self.push_stack.pop()
        # else:
        #     return self.help.pop()


        """

        if self.empty():
            raise RuntimeError("queue is empty ")

        self._size -= 1

        if self.help.is_empty():
            """
            全部 倒入 help 栈里面,每次从 help栈 取值就可以了.
            """
            while not self.push_stack.is_empty():
                self.help.push(self.push_stack.pop())
        return self.help.pop()

    def empty(self):
        return self._size == 0

    def qsize(self):
        """
        队列大小
        :return:
        """
        return self._size

    def dao(self):
        """
        倒数据 行为
        一次全 导入完.

        如果 help 不为空,一定不能倒入 数据....!!!!  直接return
        :return:
        """

        if not self.help.is_empty():
            return

        while not self.push_stack.is_empty():
            self.help.push(self.push_stack.pop())




def test_mystack():
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.peek())
    print(f"stack.pop():{stack.pop()}")
    print(stack.peek())

    print(f"stack.pop():{stack.pop()}")

    print(stack.peek())

    print(f"stack.pop():{stack.pop()}")

    print(stack.peek())

    print(f"stack.pop():{stack.pop()}")

    print(stack.peek())

    print(stack.pop())


def test_myqueue():
    q = MyQueue()

    q.put(1)
    q.put(2)
    print(f"q.qsize():{q.qsize()}")
    q.put(3)
    q.put(4)
    q.put(5)

    print(f"q.qsize():{q.qsize()}")

    print(q.get())
    print(f"q.qsize():{q.qsize()}")
    print(q.get())
    print(f"q.qsize():{q.qsize()}")
    print(q.get())
    print(q.get())
    print(f"q.qsize():{q.qsize()}")

    print(q.get())
    print(q.get())

    pass


if __name__ == '__main__':


    test_myqueue()
    pass
