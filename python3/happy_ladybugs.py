#!/bin/python3

### INCOMPLETE - passing 9/12 testcases

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):

    if len(b) < 2 or is_happy(b): 
        return "YES"
    
    counts = {}
    has_space = False
    for i in b:
        if i == "_":
            has_space = True
        elif i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1

    if 1 in counts.values() or not has_space:
        # print("NO")
        return "NO"
    # print("YES")    
    return "YES"

def is_happy(b):
    if b[0] != b[1]:
        return False
    for i in range(1, len(b)-1):
        if b[i] != b[i+1] and b[i] != b[i-1]:
            return False
    return b[-1] == b[-2]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
