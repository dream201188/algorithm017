#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]
            else:
                map[num] = i
        return []
# @lc code=end

