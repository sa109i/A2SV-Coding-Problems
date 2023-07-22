#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swapCount = 0
    for j in range(len(a)):
        for i in range(len(a)):
            if i + 1 < len(a) and a[i] > a[i + 1]:
               a[i], a[i + 1] = a[i + 1], a[i]
               swapCount += 1
            else:
               continue

    print(f"Array is sorted in {swapCount} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a) - 1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
