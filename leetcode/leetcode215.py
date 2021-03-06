# -*- coding: utf-8 -*- 
"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



1 方法1 :排序 解决 ,比较傻

"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        left, right = 0, len(nums) - 1

        while True:

            pos = self.partition(nums, left=left, right=right)

            current_m_large = pos + 1
            if k == current_m_large:
                # 刚好 第k 大
                return nums[pos]
            elif k < current_m_large:
                # 在前面继续找
                right = pos - 1
            else:
                # 在 后面 继续 找
                left = pos + 1
                pass

    @staticmethod
    def partition(array: List[int], left: int, right: int) -> int:
        """
        把 大的元素 放在 前面 ,小的元素 放到 后面.
        array   partition
        xxx >= array[left]  > xxxx

        返回 这个 数组的小标
        :param array:
        :param left:
        :param right:
        :return:
        """
        # 临时变量
        temp = array[left]

        while left < right:
            while left < right and array[right] < temp:
                right = right - 1
            array[left] = array[right]

            while left < right and array[left] >= temp:
                left = left + 1
            # 把大的数字 放到右边
            array[right] = array[left]

        array[left] = temp
        return left


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    s = Solution()

    ret = s.findKthLargest(nums, k=4)
    print(f"ret:{ret}")

    nums = [3, 2, 1, 5, 6, 4]
    rt = s.findKthLargest(nums, k=2)

    print(f"ret:{rt}")

    pass
