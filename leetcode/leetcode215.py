# -*- coding: utf-8 -*- 


"""

leetcode  215
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 先排序 在取值,解决问题
        nums.sort(reverse=True)
        return nums[k - 1]


class Solution2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lenth = len(nums)

        left, right = 0, lenth - 1

        pov = self.partion(nums, left, right)

    @staticmethod
    def partion(nums, left, right):
        index = 0

        # 选第一个数字 做为枢轴
        pov = nums[left]

        while left < right:
            pass

        pass

        return index


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    s = Solution()

    ret = s.findKthLargest(nums, k=4)
    print(f"ret:{ret}")

    nums = [3, 2, 1, 5, 6, 4]
    rt = s.findKthLargest(nums, k=2)

    print(f"ret:{rt}")

    pass
