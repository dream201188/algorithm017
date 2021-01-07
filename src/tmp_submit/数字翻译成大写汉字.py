#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : num_to_chinese.py
# @Author: meta
# @Contact : metashen@qq.com
# @Date  : 20-3-28下午9:48
# @Desc  : 阿拉伯数字代表的金额， 转换为大写数字


limit_len1 = 16  # 不超过一万兆
limit_len2 = 2  # 小数位不超过两位

dictionary = {
    '0': '零',
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖'
}

level1 = {
    1: '圆',
    2: '万',
    3: '亿',
    4: '兆'
}

level2 = {
    2: '拾',
    3: '佰',
    4: '仟'
}

level3 = {
    1: '角',
    2: '分'
}


def query():
    while 1:
        ans = str(input('请输入不超过一万兆的金额, 小数位不超过两位: '))
        if len(ans.split('.')[0]) <= limit_len1 \
                and len(ans.split('.')[1]) <= limit_len2:
            return ans


def process_integer(num_integer):
    pre = []
    length = len(num_integer)
    if length <= 4:
        pre.append(num_integer)
    else:
        extra = length % 4
        if extra != 0:
            pre.append(num_integer[0: extra])
            length = length - extra
            start, end = extra, 4 + extra
        else:
            start, end = 0, 4
        while length:
            pre.append(num_integer[start: end])
            start += 4
            end += 4
            length -= 4
    return pre


def per_conver(num):
    length = len(num)
    flag = True

    # Special
    # deal with '0000'
    if num == '0000':
        return ''
    # deal with '1000'
    if num[1:] == '000':
        return dictionary[num[0]] + level2[4]

    # Normal
    res, p = '', length
    for i in range(0, length):
        # deal with prefix is '0'
        if (res == '' or res == dictionary[num[i]]) and num[i] == '0':
            # only one '0'
            if flag:
                res += dictionary[num[i]]
                flag = False
            p -= 1
            continue
        # deal with '1001'
        if i + 1 < length and num[i + 1] == '0' and num[i] == '0':
            p -= 1
            continue
        # deal with '1010' '1110';各位是0
        if i == length - 1 and num[i] == '0':
            continue
        res += dictionary[num[i]]
        if p > 1 and num[i] != '0':
            res += level2[p]
        p -= 1
    return res


def convert_integer(ans_int):
    res = ''
    p = len(ans_int)
    for i in ans_int:
        per_res = per_conver(i)
        res += per_res
        if p > 0 and per_res != '':
            res += level1[p]
        p -= 1
    return res


def convert_float(num_float):
    res = ''
    for i in range(0, len(num_float)):
        res += dictionary[num_float[i]]
        if (i + 1) <= 2:
            res += level3[i + 1]
    return res


def convert():
    number = query()
    res = ''
    if '.' in number:
        num_split = number.split('.')
        num_integer = num_split[0]
        num_float = num_split[1]
        ans_int = process_integer(num_integer)
        print(ans_int)
        # Convert integer
        res += convert_integer(ans_int)
        # Convert float
        res += convert_float(num_float)
    else:
        ans_int = process_integer(number)
        res += convert_integer(ans_int)
    res += '整'
    print(res)


if __name__ == '__main__':
    convert()
