#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def gameWithCells(n, m):
    # 
    # this works for n or m = 1 and any other m or n
    # also works for n & m even...
    # odd numbers seem to trip it up...
    # return max(math.ceil((n * m) / 4), math.ceil(n/2), math.ceil(m/2))
    
    
    # x x x x x
    # x x x x x
    # x x x x x
    # so 5 * 3 would need 3 across, 2 down, 3*2 for all...
    # ceil(n/2) * ceil(m/2)
    return math.ceil(n/2) * math.ceil(m/2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
