#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# i j       -> ij, ji                                           = 2  -> count * count - 1
# i j n     -> ij, ji, in, ni, jn, nj                           = 6  -> count * count - 1
# i j n k   -> ij, ji, in, ni, ik, ki, jn, nj, jk, kj, nk, kn   = 12 -> count * count - 1

def solve(a):
    # Write your code here
    c_dict = {}
    summation = 0
    for x in a:
        if x not in c_dict.keys():
            cou = a.count(x)
            if cou > 1:
                c_dict[x] = 0
                summation += cou * (cou-1)
    # total = 0
    # for x in c_dict.keys():
    #     total += c_dict[x] * (c_dict[x] - 1)
    # return total
    return summation


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
