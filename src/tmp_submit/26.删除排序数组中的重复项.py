#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
# [0,0,1,1,1,2,2,3,3,4]
# [0,1,2,3,4,2,2,3,3,4]
# i, j = 0, 1
# nums[j] != nums[i]
#     i += 1
#     nums[i] = nums[j]
# j += 1


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


# @lc code=end
