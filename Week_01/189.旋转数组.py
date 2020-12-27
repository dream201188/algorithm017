#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    from typing import List
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        tmp = nums[:]; nums, tmp = tmp, nums; n = len(nums)
        for i, num in enumerate(nums):
            tmp[(i + k) % n] = num

    def rotate(self, nums: List[int], k: int) -> None:
        counter = 0; n = len(nums); k = k % n ; start = 0;
        if n == 0 or k % len(nums) == 0: return
        while counter < n:
            current_index = start
            current_num = nums[start]
            while True:
                next_index = (current_index + k) % n
                next_num = nums[next_index]
                nums[next_index] = current_num
                current_index = next_index
                current_num = next_num
                counter += 1
                if current_index == start:
                    break
            start += 1
        print(nums)

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())




if __name__ == "__main__":
    s = Solution()
    s.rotate([1,2,3,4], 2)

# @lc code=end

