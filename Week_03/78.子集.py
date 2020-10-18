#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#


# @lc code=start
class Solution(object):

    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + tmp for tmp in res]
        return res


# @lc code=end
