#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recur(left, right, path):
            # tominator
            if left == n and right == n:
                ans.append(path)
                return
            # process
            # drill down
            if left < n: recur(left + 1, right, path + '(')
            if right < left: recur(left, right + 1, path + ')')

        recur(0, 0, '')
        return ans


# @lc code=end

