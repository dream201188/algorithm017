# 一、二、三、四、五、六、七、八、九、十
# 壹、贰、叁、肆、伍、陆、柒、捌、玖、拾
num_map = {
            '一':1, '壹':1, '二':2, '贰':2, '三':3, '叁':3, '四':4, '零' : 0,
            '肆':4, '五':5, '伍':5, '六':6, '陆':6, '七':7, '柒':7, '八':8, '捌':8, '九':9, '玖':9
        }
unit_map = {
    '十': 10, '拾':10, '百':100, '千':1000, '仟' : 1000,
    '万':10000,'萬' : 10000, '亿':100000000, '億':100000000,'兆' : 1000000000000
}

#一亿一千一百二十三万四千五百六十七
# 7 60 500 4000 10000 3 20 100 1000  100000000 1
def conver(s):
    unit, stack = 1, []
    for tmp in s[::-1]:
        if tmp in unit_map:
            unit = unit_map.get(tmp)
            if unit == 10000 or unit == 100000000:
                stack.append(unit)
                unit = 1
        else:
            num = num_map.get(tmp)
            stack.append(num * unit)
    if unit == 10:
        stack.append(10)

    ans = tmp = 0
    while stack:
        num = stack.pop()
        if num == 10000 or num == 100000000:
            ans += tmp * num
            tmp = 0
        else:
            tmp += num

    ans += tmp

    return ans

# TODO: make a full unittest
def test():
    test_dig = ['八',
                '十一',
                '一百二十三',
                '一千二百零三',
                '一万一千一百零一',
                '十万零三千六百零九',
                '一百二十三万四千五百六十七',
                '一千一百二十三万四千五百六十七',
                '一亿一千一百二十三万四千五百六十七',
                '一百零二亿五千零一万零一千零三十八']
    for cn in test_dig:
        x = conver(cn)
        print(cn, x)


if __name__ == '__main__':
    test()
    # pass




