# -*- coding: utf-8 -*-
"""
 * file: bubble_sort
 * Creator: lxy
 * Date: 2020-02-27
 * Time: 23:55
"""


def bubble_sort(args):
    if len(args) < 1:
        return []
    num = 0
    for i in range(len(args) - 1):
        flag = False
        for j in range(len(args) - i - 1):
            num = num + 1
            print(num)
            if args[j] > args[j + 1]:
                flag = True
                args[j], args[j + 1] = args[j + 1], args[j]

        if not flag:
            return args
    return args


if __name__ == '__main__':
    l1 = [1, 8, 2, 4, 5, 9, 3, 7]
    l2 = bubble_sort(l1)
    print(l2)
