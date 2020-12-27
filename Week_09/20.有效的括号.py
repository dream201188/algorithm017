#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        pairs = {'}':'{', ']':'[', ')':'('}
        for kuohao in s:
            if kuohao not in pairs:
                stack.append(kuohao)
            else:
                if not stack or stack.pop() != pairs[kuohao]:
                    return False

        return not stack

    # 先报左括号入栈
    def isValid(self, s: str) -> bool:
        stack = list()
        dic = {'{':'}', '[':']', '(':')'}
        for c in s:
            if c in dic:
                stack.append(c)
            elif not stack or dic[stack.pop()] != c:
                return False
        return not stack

# @lc code=end

