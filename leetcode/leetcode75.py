#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@User    : frank 
@Time    : 2019/9/24 21:24
@File    : leetcode75.py
@Email  : frank.chang@xinyongfei.cn



https://leetcode-cn.com/problems/sort-colors/




给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

from typing import List
import random
from loguru import logger


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        时间 复杂度 O(n)
        空间复杂度   O(1)
        """
        # 分别存放 0,1,2 出现的次数,频率
        zero, one, two = 0, 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                zero = zero + 1
            elif num == 1:
                one += 1
            elif num == 2:
                two += 1
            else:
                pass
                logger.error(f"unexpected value :{num}")

        for i in range(0, zero):
            nums[i] = 0

        for i in range(zero, zero + one):
            nums[i] = 1

        for i in range(zero + one, zero + one + two):
            nums[i] = 2


class Solution2:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        只扫描数组一遍, 完成排序


        时间 复杂度 O(n)
        空间复杂度   O(1)
        """

        # nums[0,..zero] ===   0
        zero = -1

        # nums[two, ..n-1] ==  2
        two = len(nums)

        # nums [zero +1, i-1]  ==1
        i = 0
        while i < two:

            if nums[i] == 1:
                i += 1
                pass
            elif nums[i] == 2:
                two = two - 1
                nums[i], nums[two] = nums[two], nums[i]
                pass
            else:
                # nums[i] ==0 的情况
                nums[zero + 1], nums[i] = nums[i], nums[zero + 1]
                zero += 1
                i = i + 1


if __name__ == '__main__':
    nums = [0, 2, 1, 2, 0, 1, 2, 0, 0, 1, 2, 2]
    random.shuffle(nums)

    print(f"nums:{nums}")

    s = Solution2()
    s.sortColors(nums)

    print(f"nums:{nums}")
    pass
