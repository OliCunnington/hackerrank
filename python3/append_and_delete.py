#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    # check similarities
    sim = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            sim += 1
        else:
            break
    # len(s) - sim + len(t) - sim <= k -> Yes
    # else No
    # ??
    return "Yes" if (len(s) + len(t) - (2* sim)) <= k else "No"
    
    ## oh wait no, "the exact number of operations that must be performed"
    ## so the operations, with an even remainder?
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
