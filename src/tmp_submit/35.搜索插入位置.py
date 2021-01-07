#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution:
    from typing import List

    # 暴力法：但是也很巧妙，数组有序，上一个没有相等，当前一个num要么等要么大于目标，
    # 则目标就在当前的位置上

    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)


    #二分搜索，要么直接能找到位置，要么left比最大的大，要么right比最小的小，
    # 或者在两数之间， 最后也是left > right,left 正好是正确的位置
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    s = Solution()
    s.searchInsert([1, 3, 5, 6], 5)

# @lc code=end
