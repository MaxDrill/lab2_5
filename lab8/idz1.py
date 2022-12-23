#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    k = -1

    if not a:
        print(
            "заданный кортеж пуст",
            file=sys.stderr
        )
        exit(1)

    for i in a:
        if i < len(a) - 1:
            if a[i] % 2 == 0 and a[i + 1] % 2 == 0:
                k = i
        else:
            break

    if k == -1:
        print("Нет таких пар")
    elif k == 0:
        print("До последней пары нет чисел")

    for i in range(0, k):
        print(a[i])