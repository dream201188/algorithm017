#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#


# @lc code=start
class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            a = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                b = ord(num2[j]) - ord('0')
                sum = res[i + j + 1] + a * b
                res[i + j + 1] = sum % 10
                res[i + j] += sum // 10
        result = []
        for k in range(m + n):
            if k == 0 and res[k] == 0:
                continue
            result.append(str(res[k]))
        return ''.join(result)


# @lc code=end
