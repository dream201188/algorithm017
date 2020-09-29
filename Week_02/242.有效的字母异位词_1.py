/*
 * @lc app=leetcode.cn id=49 lang=python
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

// @lc code=end

