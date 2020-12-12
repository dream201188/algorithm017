#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        tmp = nums[:]
        tmp, nums = nums, tmp
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            if nums[i] + nums[k - 1] + nums[k] < 0 or nums[i] + nums[j + 1] + nums[j] > 0:
                continue

            target = 0 - nums[i]
            while j < k:
                tmp = nums[j] + nums[k]
                if tmp == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1; k -= 1

                elif tmp < target: j += 1
                else: k -= 1
        print(ans)
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
# @lc code=end

