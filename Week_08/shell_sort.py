# -*- coding: utf-8 -*-
"""
 * file: insert_sort
 * Creator: lxy
 * Date: 2020-02-28
 * Time: 18:04
"""


def shell_sort(arr):
    if len(arr) < 2:
        return

    length = len(arr)
    gap = int(length / 2)
    while gap > 0:
        for i in range(gap, length, gap):
            current = arr[i]
            j = i - gap
            while j > -gap and arr[j] > current:
                arr[j + gap] = arr[j]
                j = j - gap
            arr[j + gap] = current
        gap = int(gap / 2)


if __name__ == '__main__':
    l1 = [1, 8, 2, 6, 4, 10, 5, 9, 3, 7]
    shell_sort(l1)
    print(l1)
