# -*- coding: utf-8 -*-
"""
 * file: insert_sort
 * Creator: lxy
 * Date: 2020-02-28
 * Time: 18:04
"""

num = 0
def HeapAdjust(arr, i, length):
    global num
    num = num + 1
    print("调整次数：%d" % num)
    max = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < length and arr[max] < arr[l]:
        max = l

    if r < length and arr[max] < arr[r]:
        max = r

    if max != i:
        arr[max], arr[i] = arr[i], arr[max]
        HeapAdjust(arr, max, length)


def BuildMaxHeap(arr, length):
    for i in range(length // 2 - 1, -1, -1):  # 从最后一个非叶子节点开始。进行堆调整。
        HeapAdjust(arr, i, length)


def heap_sort(arr):
    if len(arr) < 2:
        return

    length = len(arr)
    for i in range(length, 0, -1):
        BuildMaxHeap(arr, i)
        arr[0], arr[i - 1] = arr[i - 1], arr[0]


if __name__ == '__main__':
    l1 = [1, 8, 2, 14, 6, 15, 4, 2, 3, 1, 10, 5, 15, 10, 9, 3, 7]
    heap_sort(l1)
    print(l1)
