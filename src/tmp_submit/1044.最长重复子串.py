#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#


# @lc code=start
class Solution:
    """
    获取所有子串，并把长度从大到小排列；
    获取字符串的公共前缀和后缀长度
    """

    def longestDupSubstring(self, s: str) -> str:

        def get_substrs(s):
            res = set()
            for i in range(n):
                for j in range(i + 1, n + 1):
                    res.add(s[i:j])
            return sorted(list(res), key=lambda i: len(i), reverse=True)

        def get_next(son_string):
            next = [-1] * len(son_string)

            if len(son_string) > 1:  # 这里加if是怕列表越界
                next[1] = 0
                i, j = 1, 0
                while i < len(son_string) - 1:  #这里一定要-1，不然会像例子中出现next[8]会越界的
                    if j == -1 or son_string[i] == son_string[j]:
                        i += 1
                        j += 1
                        next[i] = j
                    else:
                        j = next[j]
            return next[-1], son_string[:next[-1] + 1]

        n = len(s)
        if n == 1:
            return s
        substrs = get_substrs(s)
        for s in substrs:
            res = get_next(s)
            if res[0]:
                print(res)
                return res[1]

    def longestDupSubstring(self, S: str) -> str:
        from functools import reduce
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        n = len(S)

        def test(l):
            p = pow(26, l, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:l])
            seed = {cur}
            for index in range(l, n):
                cur = (cur * 26 + A[index] - A[index - l] * p) % mod
                if cur in seed:
                    return index - l + 1
                seed.add(cur)
            return -1

        low, high = 0, n
        res = 0
        while low < high:
            mid = (low + high + 1) // 2
            pos = test(mid)
            if pos != -1:
                low = mid
                res = pos
            else:
                high = mid - 1
        return S[res:res + low]


if __name__ == "__main__":
    s = Solution()
    print(s.longestDupSubstring("asdfasdfasdf"))

# @lc code=end
