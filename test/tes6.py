#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/22 10:07
@File    : tes6.py
@Author  : frank.chang@shoufuyou.com



白鸡百钱问题



s = { (x ,y ,z) |0<=x,y ,z <=100}

 x +y +z  =100


 5*x  + 3*y  +  Z//3 = 100




"""


def fun():
    for x in range(0, 101):
        for y in range(0, 101 - x, 1):

            z = 100 - x - y

            if z % 3 == 0:
                if 5 * x + 3 * y + z // 3 == 100:
                    print(x, y, z)









if __name__ == '__main__':

    fun()
    pass
    
