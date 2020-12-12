#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start

from typing import List


class Solution:
    """暴力循环超时"""
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        length, ans = len(height), 0
        for i in range(1, length - 1):
            j = i - 1; k = i + 1
            while j > -1:
                left = max(height[j], height[i])
                j -= 1
            while k < length:
                right = max(height[i], height[k])
            ans += min(left, right) - height[i]
        return ans

    """
    想用栈，实际上是动态办法，找的每个柱子左右最近最大高度，
    只算每个柱子存储的雨水
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        length, ans = len(height), 0
        left, right, stack = [-1] * length, [-1] * length, [-1]

        for i in range(length):
            left[i] = stack[-1]
            if stack[-1] <= height[i]:
                stack.append(height[i])
        stack = [-1]
        for i in range(length - 1, -1, -1):
            right[i] = stack[-1]
            if stack[-1] <= height[i]:
                stack.append(height[i])

        for i in range(length):
            ans += max(0, min(left[i], right[i]) - height[i])
        return ans

    """
    是上面办法的简化，想法一样，只是程序上进行精简
    实际上是动态办法，找的每个柱子左右最近最大高度，
    只算每个柱子存储的雨水
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        length, ans = len(height), 0
        left, right = [-1] * length, [-1] * length
        left[0] = height[0]
        for i in range(1, length):
            left[i] = max(height[i], left[i - 1])
        right[-1] = height[-1]
        for i in range(length -2 , -1, -1):
            right[i] = max(height[i], right[i + 1])

        for i in range(length):
            ans += min(left[i], right[i]) - height[i]
        return ans


    """
    单调递减栈，一遍循环解决：
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        length, ans = len(height), 0
        stack = []
        for i in range(length):
            while stack and height[stack[-1]] < height[i]:
                base_height_index = stack.pop() # 用来盛水的高度
                if not stack:
                    break
                left_bound = stack[-1]
                right_bound = i
                width = right_bound - left_bound - 1
                diff = min(height[right_bound], height[left_bound]) - height[base_height_index]
                ans += width * diff
            stack.append(i)
        return ans
# @lc code=end
