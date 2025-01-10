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
    # a_ = []
    # flag = False
    # for i in range(len(a)):
    #     a_.append([a[i]])
    #     for j in range(len(a)):
    #         if not i == j:
    #             for k in range(len(a_)):
    #                 if abs(a[k]-a[j]) > 1:
    #                     flag = False
    #                     break
    #                 else:
    #                     flag = True
    #             if flag: a_[i].append(a[j])
    #         flag = False
            
    # # Write your code here
    # return max([len(x) for x in a_])

    counts = {}
    for i in list(set(a)):
        counts[i] = a.count(i)
    
    # if len(list(counts.keys())) == 1 : return counts[a[0]]
    
    sumPairs = []    
    for i in counts.keys():
        for j in counts.keys():
            if abs(i-j)<=1 and not i == j:
                sumPairs.append(counts[i] + counts[j])
        sumPairs.append(counts[i])
    return max(sumPairs)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
