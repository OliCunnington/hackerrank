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
    ops = len(s) + len(t) - (2* sim)
 
    # this checks if you have enough operations, and then the remaining operations
    # are even, allowing add/remove or remove/add operation pairs...   
    return "Yes" if  ops <= k and (k - ops) % 2 == 0 else "No"
    # still doesnt like it...
 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
