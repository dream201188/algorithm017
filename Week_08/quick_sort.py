# -*- coding: utf-8 -*-
"""
 * file: quick_sort
 * Creator: lxy
 * Date: 2020-02-27
 * Time: 23:55

 思路：最右边的是个楔子值，放到独立内存；找个哨兵j从最左边到最右边倒第二个挨个找，
       还有一个哨兵i是用来标志比楔子小的数的位置，i默认low的左边
      只要找到小于楔子的就把他放在i+1的位置，i永远是要找到新位置的左边一个，
      到最后已经没有比楔子小的了，i在最后一个比楔子小的位置上，i+1是楔子要放的位置，返回i+1，并且跟楔子换位
"""


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


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
    l1 = [1, 8, 2, 4, 5, 9, 3, 7]
    quick_sort_test(l1)
    print(l1)
