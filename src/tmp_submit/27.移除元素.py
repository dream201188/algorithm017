#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                if i != j:
                    nums[i] = nums[j]
                i += 1
            j += 1
        return i


# @lc code=end
