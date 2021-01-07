#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        j, ans, n, sub_set = 0, -1, len(s), set(s[0])
        for i in range(n):
            while j + 1 < n and s[j + 1] not in sub_set:
                sub_set.add(s[j + 1])
                j += 1
            ans = max(ans, j - i + 1)
            sub_set.remove(s[i])
        print(ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    s.lengthOfLongestSubstring('abcabcbb')


# @lc code=end

