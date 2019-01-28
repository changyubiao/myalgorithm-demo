#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/12 00:59
@File    : has_circle.py
@Author  : frank.chang@shoufuyou.com


https://leetcode.com/problems/linked-list-cycle/



https://leetcode.com/problems/linked-list-cycle/




141. Linked List Cycle
Easy

1231

93

Favorite

Share
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.




Follow up:

Can you solve it using O(1) (i.e. constant) memory?

Accepted
340,579
Submissions
971,443

"""


class LinkNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution1:
    """
    思路分析:
    判断一个单链表是否有环,
    可以用 set 存放每一个 节点, 这样每次 访问后把节点丢到这个集合里面.
    其实 可以遍历这个单链表, 访问过后,
    如果这个节点 不在 set  里面, 把这个节点放入到 set 集合里面.
    如果这个节点在  set 里面 , 说明曾经访问过, 所以这个链表有重新 走到了这个节点, 因此一定有环.

    如果链表都走完了, 把所有的节点都放完了. 还是没有重复的节点, 那说明没有环.

    """

    def hasCycle(self, head):

        mapping = set()

        flag = False

        p = head

        while p:

            if p not in mapping:
                mapping.add(p)
            else:
                flag = True
                break
            p = p.next

        return flag


class Solution:
    """

    """

    def hasCycle(self, head):

        flag = False
        if head is None or head.next is None or head.next.next is None:
            return flag

        fast = head.next.next
        slow = head.next

        while fast is not slow:

            if fast.next is None or fast.next.next is None:
                # no circle
                return flag
            fast = fast.next.next
            slow = slow.next

        # 相遇肯定有环
        if fast is slow:
            # hasCircle
            flag = True

        return flag


if __name__ == '__main__':
    pass
