# -*- coding: utf-8 -*-
"""
 * file: heap_sort2
 * Creator: lxy
 * Date: 2020-02-29
 * Time: 20:14
"""

num = 0


def heapify(arr, n, i):
    global num
    num = num + 1
    print("调整次数：%d" % num)
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [1, 8, 2, 14, 6, 15, 4, 2, 3, 1, 10, 5, 15, 10, 9, 3, 7]
heapSort(arr)
n = len(arr)
print("排序后")
print(arr)
