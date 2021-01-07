#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#


# @lc code=start
class Solution:

    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if not A and not B:
            return True

        def get_next(son_string):
            #求next数组
            next = [-1] * len(son_string)
            next[1] = 0
            if len(son_string) > 1:  # 这里加if是怕列表越界
                i, j = 1, 0
                while i < len(son_string) - 1:  #这里一定要-1，不然会像例子中出现next[8]会越界的
                    if j == -1 or son_string[i] == son_string[j]:
                        i += 1
                        j += 1
                        next[i] = j
                    else:
                        j = next[j]
            return next

        def kmp(mom_string, son_string):
            next = get_next(B)
            # kmp框架
            m = s = 0  #母指针和子指针初始化为0
            ans = []
            # 原来的基础上完善，可以循环找更多的匹配串
            while m < len(mom_string):
                if s == len(
                        son_string) - 1 and mom_string[m] == son_string[s]:  #匹配成功；子串最后一位正好匹配上了，
                    return True

                if s == -1 or mom_string[m] == son_string[s]:
                    m += 1
                    s += 1
                else:
                    s = next[s]
            return False

        return kmp(A + A, B)

    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A


# @lc code=end
