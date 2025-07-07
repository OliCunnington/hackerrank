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
    # s = list(set(s))
    # Write your code here
    ## take s[0], remove every element that sums to multiple of k
    
    # for i in s[1:]:
    #   s.remove(i) if sum(s[0], i) % k == 0
    
    ## take s[1] ...
    ## repear until s[-1]
    
    ##  elements before will sum to non-mult of k
    
    ## whut uboot ze others?!
    ## like, removed elements
    ## do it again starting with s[1] ? ignore s[0]
    ## do it again
    ## return max len
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
