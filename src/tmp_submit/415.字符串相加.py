#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#


# @lc code=start
class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        res = []
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            sum = a + b + carry
            carry = sum // 10
            res.append(str(sum % 10))
            i, j = i - 1, j - 1

        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)

    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        res = ''
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            sum = a + b + carry
            carry = sum // 10
            res = str(sum % 10) + res
            i, j = i - 1, j - 1

        res = '1' + res if carry == 1 else res
        return res


# @lc code=end
