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



1 方法1 :排序 解决 ,比较傻  ,

"""

from typing import List


class Solution_01:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        left, right = 0, len(nums) - 1

        while True:

            pos = self.partition(nums, left=left, right=right)

            current_m_large = right - pos + 1
            if k == current_m_large:
                # 刚好 第k 大
                return nums[pos]
            elif k < current_m_large:
                # 在 后面 继续 找
                left = pos + 1
            else:
                # 在前面继续找
                right = pos - 1
                pass

    @staticmethod
    def partition(array: List[int], left: int, right: int) -> int:
        """


        array   partition

        xxx <= array[left]  < xxxx


        保证 A[left] 左边的元素 都小于等于A[left],   保证A[left] 右边的元素 都大于 A[left]

         返回 这个 数组的小标
        :param array:
        :param left:
        :param right:
        :return:
        """

        # 临时变量
        temp = array[left]

        while left < right:
            # 这个 left < right 这个条件不能丢
            while left < right and array[right] > temp:
                right = right - 1
            # 把 小的数字放在左边
            array[left] = array[right]

            # 这个left < right 这个条件不能丢
            while left < right and array[left] <= temp:
                left = left + 1
            # 把大的数字 放到右边
            array[right] = array[left]

        array[left] = temp

        return left


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

    solution = Solution()

    print(solution.findKthLargest(nums, k=4))

    pass
