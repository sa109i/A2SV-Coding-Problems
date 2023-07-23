#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    lastvalue = arr[-1]
    for i in reversed(range(n)):
        if i !=0 and arr[i - 1] > lastvalue:
            arr[i] = arr[i - 1]
            print(' '.join([str(i) for i in arr]))
        else:
            arr[i] = lastvalue
            print(' '.join([str(i) for i in arr]))
            break


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
