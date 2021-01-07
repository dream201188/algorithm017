#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    from typing import List

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length, ans = len(height), 0
        for i in range(1, length - 1):
            j = i - 1
            k = i + 1
            left = height[i]
            right = height[i]
            while j > -1:
                left = max(height[j], left)
                j -= 1
            while k < length:
                right = max(height[k], right)
                k += 1
            print(min(left, right))
            ans += min(left, right) - height[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# @lc code=end
