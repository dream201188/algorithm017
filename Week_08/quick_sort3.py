# -*- coding: utf-8 -*-
"""
 * file: quick_sort
 * Creator: lxy
 * Date: 2020-02-27
 * Time: 23:55

 思路： 左边哨兵i，右边哨兵j，最左边的i是楔子值，已经放到单独内存放置，位置上是个坑；
       首先从右边起开始移动j，找出第一个比楔子小的位置，此时j停留，不做操作，
       再去从左边找第一个比楔子大的位置i，i停留住；
       然后如果 还有 i < j， 那么i j swap；
       如果i == j了，说明第一个分割点找到了，楔子位置与分割点位置进行交换
"""


def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]

    while i < j:
        while (i < j) and arr[j] >= pivot:
            j = j - 1

        while i < j and arr[i] <= pivot:
            i = i + 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def quick_sort_test(arr):
    length = len(arr)
    if length < 2:
        return

    low = 0
    high = length - 1
    quick_sort(arr, low, high)
    return


if __name__ == '__main__':
    l1 = [1, 8, 11, 2, 10, 4, 5, 12, 9, 13, 3, 7]
    quick_sort_test(l1)
    print(l1)
