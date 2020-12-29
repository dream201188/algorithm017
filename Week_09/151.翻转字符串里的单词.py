#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split()))

# 多个空格保留，两种办法

# 第一个办法是当场想的遇到空格就把前面的字母添加到数组tmp里；一直数空格数
# 遇到字母后，如果空格数大于0，把空格添加到数组tmp里，一直数字母数
def split_str(line):
    tmp = []
    char_num = 0
    space_num = 0
    line = line.strip()

    line += ' ' # 防止最后一个单词不能进入到数组
    for i, char in enumerate(line):
        if char == ' ':
            if char_num > 0:
                tmp.append(line[i - char_num:i])
                char_num = 0
            space_num += 1
        else:
            char_num += 1
            if space_num > 0:
                tmp.extend([' ' * space_num])
                space_num = 0
    i, j = 0, len(tmp) - 1
    while i < j:
        tmp[i], tmp[j] = tmp[j], tmp[i]
        i += 1; j -= 1
    new_line = ''.join(tmp)
    return new_line

# 第二种：跟上面比是倒着数遇到第一个单词就增加到数组，正好是倒序了
# 用双指针办法，i遇到空格后，j还是最末尾，把单词加进来；
# 这时候让j直接指向右边第一个空格
def split_str2(line):
    # 先把开头和末尾的空格过滤掉
    i, j = 0, len(line) - 1
    while line[i] == ' ':
        i += 1
    while line[j] == ' ':
        j -= 1
    line = line[i:j + 1]


    i = j = len(line) - 1
    tmp = []
    while i >= 0:
        while i >= 0 and line[i] != ' ':
            i -= 1
        tmp.append(line[i + 1:j + 1])
        j = i
        while line[i] == ' ':
            i -= 1
        if i < j: # 最后当i==-1时候，也会跳出但是没有空格所以判断一下
            tmp.append(line[i + 1:j + 1])
        j = i
    print tmp
    return ''.join(tmp)

# @lc code=end

