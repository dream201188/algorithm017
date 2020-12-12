# -*- coding: utf-8 -*-
"""
 * file: insert_sort
 * Creator: lxy
 * Date: 2020-02-28
 * Time: 18:04
"""


def insert_sort(arr):
    if len(arr) < 2:
        return arr

    length = len(arr)
    for i in range(1, length):
        current = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > current:
                arr[j + 1] = arr[j]
            else:
                break
        arr[j + 1] = current
    return arr


def insert_sort2(arr):
    if len(arr) < 2:
        return arr

    length = len(arr)
    for i in range(1, length):
        current = arr[i]
        j = i - 1
        while j > -1 and arr[j] > current:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = current
    return arr


if __name__ == '__main__':
    l1 = [1, 8, 2, 6, 4, 10, 5, 9, 3, 7]
    insert_sort2(l1)
    print(l1)
