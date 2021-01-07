#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            l = dfs(root.left)
            r = dfs(root.right)
            selected = root.val + l[0] + r[0] # 选择当前节点，两个儿子都不选
            notSelected = max(l[0], l[1]) + max(r[0], r[1]) # 不选当前节点，儿子里面挑最大的
            return (notSelected, selected)

        res = dfs(root)
        return max(res[0], res[1])

# @lc code=end

