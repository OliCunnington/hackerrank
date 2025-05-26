#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    s = 0
    for i in range(1, len(arr)):
        # j = 0
        while i >= 1:
            if arr[i-1] > arr[i]:
                s += 1
                arr[i], arr[i-1] = arr[i-1], arr[i]
            i -=1
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
