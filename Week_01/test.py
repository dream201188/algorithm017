"""
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
剑指 Offer 12. 矩阵中的路径
"""
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word: return False
        m, n, k = len(board), len(board[0]), len(word)
        def dfs(i, j, level):
            if not -1 < i < m or not -1 < j < n or board[i][j] != word[level]:
                return False
            if level == k - 1: return True
            ans = False
            board[i][j] = ''
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(i + x, j + y, level + 1):  # | 不具备短路性质
                    ans = True
                    break
            board[i][j] = word[level]
            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False

    def exist(self, board, word):
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


"""
剑指 Offer 66. 构建乘积数组
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
"""
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a); b,tmp = [1] * n, 1
        b[1:] = [a[i - 1] * b[i - 1] for i in range(1, n)] # 构建一个新的字符串， b[i - 1] 相当于还是1
        for i in range(1, n):
            b[i] = a[i - 1] * b[i - 1]
        for i in range(n - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b

"""
剑指 Offer 48. 最长不含重复字符的子字符串
https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        length = len(s); res = tmp = 0; dic = {}; dp = [0] * (length + 1)
        for j in range(0, length):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            if dp[j] < j - i:
                dp[j + 1] = dp[j] + 1
            else:
                dp[j + 1] = j - i
        return max(dp)

    # 简化空间
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        length = len(s); res = tmp = 0; dic = {};
        for j in range(0, length):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            if tmp < j - i:
                tmp += 1
            else:
                tmp = j - i
            res = max(res, tmp)
        return res

    # 双指针：
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res



"""
剑指 Offer 26. 树的子结构
https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
"""
class Solution:
    # 完全根据递归定义怼出来的代码；
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False

        def dfs(big, small):
            if big.val != small.val:
                return False
            if small.left: # 小的如果有左子树就比较；没有就不比较
                if not big.left:
                    return False
                if not dfs(big.left, small.left): # 都有左子树
                    return False
            if small.right:# 小的如果有右子树就比较；没有就不比较
                if not big.right:
                    return False
                if not dfs(big.right, small.right):# 都有右子树
                    return False
            return True

        def dfs2(A, B): # 牛逼的是用第二个dfs
            if dfs(A, B): return True
            if A.left and dfs2(A.left, B): return True
            if A.right and dfs2(A.right, B): return True
            return False

        return dfs2(A,B)


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))












if __name__ == "__main__":
    s = Solution()
    s.exist([["a"]], "ab")
