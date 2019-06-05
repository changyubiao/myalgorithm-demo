#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/10 11:17
@File    : test_Semaphore.py
@Author  : frank.chang@shoufuyou.com

Semaphore   信号量


实现 是通过 threading.Condition() 来实现的, 来控制启动线程的数量.可以看看源码.

acquire()
release()

每当调用acquire()时，内置计数器-1
每当调用release()时，内置计数器+1


1 控制启动线程数量的方法


"""
import threading
import time

from threading import Semaphore, BoundedSemaphore


class HtmlParser(threading.Thread):

    def __init__(self, url, sem, name='html_parser'):
        super().__init__(name=name)
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('got html success')

        self.sem.release()


class UrlProducer(threading.Thread):

    def __init__(self, sem, name='url_produce'):
        super().__init__(name=name)
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlParser(url=f"http://www.baidu.com/item={i}",
                                     sem=self.sem
                                     )

            html_thread.start()


if __name__ == '__main__':
    sem = Semaphore(5)
    url_producer = UrlProducer(sem)
    url_producer.start()
