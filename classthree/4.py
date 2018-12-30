#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/22 15:16
@File    : dog_cat.py
@Author  : frank.chang@shoufuyou.com



猫狗队列 【 题目】 宠物、 狗和猫的类如下：
public class Pet { private String type;
public Pet(String type) { this.type = type; }
public String getPetType() { return this.type; }
}
public class Dog extends Pet { public Dog() { super("dog"); } }
public class Cat extends Pet { public Cat() { super("cat"); } }




实现一种狗猫队列的结构，
要求如下： 用户可以调用add方法将cat类或dog类的
实例放入队列中；

用户可以调用pollAll方法，      将队列中所有的实例按照进队列的先后顺序依次弹出；
用户可以调用pollDog方法，      将队列中dog类的实例按照进队列的先后顺序依次弹出；
用户可以调用pollCat方法，      将队列中cat类的实 例按照进队列的先后顺序依次弹出；
用户可以调用 isEmpty 方法，    检查队列中是否还有dog或cat的实例；
用户可以调用isDogEmpty方法，   检查队列中是否有dog类的实例；
用户可以调用isCatEmpty方法，   检查队列中是否有cat类的实例。





python  Queue  没有提供  获得队首 的方法
"""

from queue import Queue as  _Queue
from datetime import datetime

import time


def _get_curtime():
    """工具类 返回一个时间字符串
    返回一个时间字符串

    这个如果同时进入 可能 在秒级别的 话,可能会 有冲突.

    '20181222172324'
    :return:  str   '20181222172324'
    """
    t = str(datetime.now())

    t1 = t.split('.')[0]

    t2 = t1.replace('-', '').replace(":", '').replace(' ', '')
    # print(f'curtime:{t2}')
    return t2


def get_timestamp():
    """
    获取当前时间戳, 毫秒级别 , 更小粒度
    :return:
    """
    now = lambda: int(round(time.time() * 100000))

    return now()


class Pet:

    def __init__(self, type_name):
        self.type_name = type_name

    def get_type(self):
        return self.type_name


class Dog(Pet):

    def __init__(self, type_name="dog"):
        super().__init__(type_name)


class Cat(Pet):

    def __init__(self, type_name="cat"):
        super().__init__(type_name)


"""
解决 方法

设计思路 :  猫狗队列   


设计一个  猫队列, 狗队列,  然后每次入队列 给这个猫,狗 打一个标签,表示进入队列 的时间. 

出队列的 时候  获取 这个时间进行比较, 时间较小的 一定 是最先进入 队列的, 所以,如果有 一个队列 空了,依次另外一个队列 出队列即可. 





"""


class Queue(_Queue):

    def __init__(self, maxsize: int = 0) -> None:
        super().__init__(maxsize)

    def peek(self):
        """
        返回队列  队首 元素, 不是出队列
        :return:
        """
        item = self.queue.popleft()
        self.queue.appendleft(item)
        return item


class PetEnter:
    """
    给每个狗或者猫 打一个时间标签.
    """

    def __init__(self, pet, time_):
        """

        :param pet: pet   dog or  cat
        :param time_:  float  给pet 打一个时间标签
        """
        self.pet = pet

        self.time_ = time_

    def get_pet(self):
        return self.pet

    def get_time(self):
        return self.time_

    def getEnterType(self):
        return self.pet.get_type()

    def __str__(self):
        return f"Pet({self.pet.get_type()},{self.time_})"

    __repr__ = __str__


class DogCatQueue:

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.time_ = get_timestamp()

    def put(self, pet):
        """
        入队列的方法
        :param pet:
        :return:
        """

        cur_time = get_timestamp()

        if pet.get_type() == 'dog':
            self.dog_queue.put(PetEnter(pet, cur_time))
        elif pet.get_type() == 'cat':
            self.cat_queue.put(PetEnter(pet, cur_time))
        else:
            raise TypeError("pet is not  dog  or  not cat ")

    def pollAll(self):
        """
        将队列中所有的实例按照进队列的先后顺序依次弹出；
        :return:
        """
        if not self.dog_queue.empty() and not self.cat_queue.empty():
            dog_enter = self.dog_queue.peek()
            cat_enter = self.cat_queue.peek()

            if dog_enter.time_ < cat_enter.get_time():
                return self.dog_queue.get()
                # return self.dog_queue.get().pet
            elif dog_enter.time_ > cat_enter.get_time():
                # return self.cat_queue.get().pet
                return self.cat_queue.get()
            else:
                raise RuntimeError(f"dog_time:{dog_enter.time_} equals cat_time:{cat_enter.time_}")
        elif not self.dog_queue.empty():
            return self.dog_queue.get()
            # return self.dog_queue.get().pet

        elif not self.cat_queue.empty():
            return self.cat_queue.get()
            # return self.cat_queue.get().pet
        else:
            raise RuntimeError(f"error queue is empty")

    def pollDog(self):
        """
         将队列中dog类的实例按照进队列的先后顺序依次弹出；
        :return:
        """

        if not self.dog_queue.empty():
            dog = self.dog_queue.get()

            # return dog.get_pet()
            return dog

    def pollCat(self):
        """

        :return:
        """

        if not self.cat_queue.empty():
            cat = self.cat_queue.get()

            # return cat.get_pet()
            return cat

    def isEmpty(self):
        """
        检查队列中是否还有dog或cat的实例；

        :return:
        """

        if self.cat_queue.empty() and self.dog_queue.empty():
            return True

        return False

    def isDogEmpty(self):
        """
        检查队列中是否有dog 类的实例。
        :return:
        """

        return self.dog_queue.empty()

    def isCatEmpty(self):
        """
         检查队列中是否有cat类的实例。
        :return:
        """

        return self.cat_queue.empty()


if __name__ == '__main__':
    pass
    test = DogCatQueue()

    dog1 = Dog("dog")
    cat1 = Cat()
    dog2 = Dog("dog")
    cat2 = Cat()
    dog3 = Dog("dog")
    cat3 = Cat()

    test.put(dog1)

    time.sleep(0.1)
    test.put(cat1)
    time.sleep(0.1)

    test.put(dog2)
    time.sleep(0.1)
    test.put(cat2)

    test.put(dog3)
    test.put(cat3)

    test.put(dog1)
    test.put(cat1)
    test.put(dog2)
    test.put(cat2)
    test.put(dog3)
    test.put(cat3)

    test.put(dog1)
    test.put(cat1)
    test.put(dog2)
    test.put(cat2)
    test.put(dog3)
    test.put(cat3)

    while not test.isDogEmpty():
        enter = test.pollDog()
        print(f"{enter.get_pet().get_type()},{enter.get_time()}")

    print('***' * 23)

    while not test.isEmpty():
        enter = test.pollAll()

        print(f"{enter.get_pet().get_type()},{enter.get_time()}")
