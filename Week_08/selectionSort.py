# -*- coding: utf-8 -*-
"""
 * file: selectionSort
 * Creator: lxy
 * Date: 2020-02-28
 * Time: 18:04
"""


def selectionSort(arr):
    if len(arr) < 2:
        return arr

    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    l1 = [1, 8, 2, 4, 5, 9, 3, 7]
    selectionSort(l1)
    print(l1)
