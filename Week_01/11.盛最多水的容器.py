#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # 暴力法，超时
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        max_area = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                max_area = max(max_area, (j - i) * min(height[i], height[j]))
        return max_area

    # 双指针法
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return max_area
# @lc code=end

