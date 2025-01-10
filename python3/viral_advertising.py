#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    return viralRec(n, 1, 5, 0)
    
def viralRec(n, i, share, res):
    if n == i:
        return res + math.floor(share/2)
    else:
        return viralRec(n, i+1, math.floor(share/2)* 3, res + math.floor(share/2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
