#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#


# @lc code=start
class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        i = n - 2
        while i > -1:
            if nums[i] < nums[i + 1]:
                j = n - 1
                while j > i and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                reverse(nums, i + 1, n - 1)
                return
            i -= 1
        reverse(nums, 0, n - 1)
        return


# @lc code=end
