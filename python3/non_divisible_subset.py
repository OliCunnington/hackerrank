#!/bin/python3

import math
import os
import random
import re
import sys

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
    
    # s_c = s.copy()
    s_s = []
    
    # for j in range(len(s_c) - 1):
    #     for i in s_c[j+1:]:
    #         if (s_c[j] + i) % k == 0:
    #             s_c.remove(i)
    #     s_s.append(len(s_c))
    #     s_c = s.copy()
    
    # Kekw, i need to check each other element in list against others...
    
    # how the fuck does for x in as loop interact with as.remove(x) ?!
    
    # i need to construct the lists, not remove from copy
    # this will allow me to add an element if NONE (a+b) % k == 0
    
    for i in range(len(s) - 1):
        s_s.append([s[i]])
        for j in s[i+1:]:
            if can_insert(k, j, s_s[i]):
                s_s[i].append(j)
    
    return max(list(map(len, s_s)))
    

def can_insert(k, i, s):
    for j in s:
        if (i + j) % k == 0:
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
