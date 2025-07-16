#!/bin/python3

import math
import os
import random
import re
import sys


### INCOMPLETE - timeout on large list


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    s = list(set(s))
    
    s_s = []
    
    for i in range(len(s)):
        s_s.append([s[i]])
        for j in s:
            if can_insert(k, j, s_s[i]):
                s_s[i].append(j)
    
    return max(list(map(len, s_s)))
    

def can_insert(k, i, s):
    for j in s:
        if (i + j) % k == 0 or i == j:
            return False
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
