#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    d = {}
    di = []
    for i in range(len(a)):
        if a[i] in d.keys():
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    for k in d.keys():
        if len(d[k]) > 1:
            for i in range(len(d[k]) - 1):
                di.append(abs(d[k][i] - d[k][i+1]))
    return min(di) if len(di) != 0 else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
