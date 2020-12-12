# -*- coding: utf-8 -*-
"""
 * file: insert_sort
 * Creator: lxy
 * Date: 2020-02-28
 * Time: 18:04
"""


def merge(arr, left, mid, right, temp_arr):
    i = left
    j = mid + 1
    t = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr.append(arr[i])
            i += 1
        else:
            temp_arr.append(arr[j])
            j += 1

    while i <= mid:
        temp_arr.append(arr[i]);i += 1
    while j <= right:
        temp_arr.append(arr[j]);j += 1

    k = left
    t = 0
    while k <= right:
        arr[k] = temp_arr[t];t += 1; k += 1


def merge_sort_in(arr, left, right):
    temp_arr = []
    if left < right:
        mid = (left + right) >> 1
        merge_sort_in(arr, left, mid)
        merge_sort_in(arr, mid + 1, right)
        merge(arr, left, mid, right, temp_arr)


def merge_sort(arr):
    if len(arr) < 2:
        return

    length = len(arr)
    merge_sort_in(arr, 0, length - 1)


if __name__ == '__main__':
    l1 = [1, 8, 2, 6, 4, 10, 5, 9, 3, 7]
    merge_sort(l1)
    print(l1)
