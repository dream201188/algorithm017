#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 0, x - 1
        while left <= right:
            mid = (left + right) >> 1
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end

