#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root):
            if not root.left and not root.right:
                return 1
            min_depth = float('inf')
            if root.left:
                min_depth = min(min_depth, dfs(root.left))
            if root.right:
                min_depth = min(min_depth, dfs(root.right))
            return min_depth + 1

        return dfs(root)

# @lc code=end

