#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    value = 3
    while (True):
        if (t - value) == 0:
            return 1
        elif (t - value) < 0:
            return value - (t - 1)
        else:
            t -= value
            value *= 2
    
# do the loop on the 
# value left in t
# if (t - value) < 0:
#     do the -1 loop
# else:
#   t -= value
#   value *= 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
