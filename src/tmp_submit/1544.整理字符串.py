#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#


# @lc code=start
class Solution:

    def makeGood(self, s: str) -> str:
        if not s:
            return s
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


# @lc code=end
