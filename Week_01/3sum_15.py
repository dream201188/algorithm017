from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

    #最新自己写一遍
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
