#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a_ = []
    for i in range(len(a)):
        a_.append([])
        for j in range(len(a)):
            if abs(a[i]-a[j]) <= 1 and not i == j:
                a_[i].append(a[j])
            
            
    # Write your code here
    return max([len(x) for x in a_])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
