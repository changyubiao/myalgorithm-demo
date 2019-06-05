#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/11 11:03
@File    : 2.py
@Author  : frank.chang@shoufuyou.com



在二叉树中找到一个节点的后继节点
【题目】 现在有一种新的二叉树节点类型如下：
public class Node {
    public int value;
    public Node left;
    public Node right;
    public Node parent;

    public Node(int data) {
        this.value = data;
    }
}
该结构比普通二叉树节点结构多了一个指向父节点的parent指针。
假设有一棵Node类型的节点组成的二叉树，树中每个节点的parent指针都正确地指向自己的父节点，头节点的parent指向null。
只给一个在二叉树中的某个节点 node，请实现返回node的后继节点的函数。
在二叉树的中序遍历的序列中，node的下一个节点叫作node的后继节点。


在中序遍历中

在中序遍历中,一个节点的下一个节点 就是这个节点的后继结点.
 同理 前驱结点  也是 类似的.   是指 在中序遍历中, 某一个结点 的前面一个节点 就是 该节点的前驱结点.



                  1

            2             3
         4    5         6   7


中序遍历结果:   4 2 5 1 6 3 7


4 的后继结点是 2 ,    5 的后继结点是 1

6 的前驱结点是 1 , 6的后继结点是 3



"""



class Node:
    """
    二叉树 结点
    """

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

        # 指向父节点
        self.parent = None






if __name__ == '__main__':
    pass
    
