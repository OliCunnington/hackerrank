#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
def summingSeries(n):
    # return _summingSeriesRecursive(n) % (10**9 + 7)
    # return _summingSeriesWhile(n) % (10**9 + 7)
    # return _summingSeriesMemo(n) % (10**9 + 7)
    return n ** 2 % (10**9 + 7)


memo = {1: 1}
def _summingSeriesMemo(n):
    # this is most likely hitting recursion depth again...
    if n in memo:
        return memo[n]
    else:
        cur_sum = n ** 2 - (n-1) ** 2 + _summingSeriesMemo(n-1)
        memo[n] = cur_sum
        return cur_sum
        


def _summingSeriesWhile(n):
    # this timesout...
    total = 1
    while(n > 1):
        total += n ** 2 - (n - 1) ** 2
        n -= 1
    return total


def _summingSeriesRecursive(n):
    # doesnt work, depth limited to ~1000
    if n == 1:
        return 1
    else:
        return n**2 - (n-1)**2 + _summingSeriesRecursive(n-1)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
