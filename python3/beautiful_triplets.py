#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    
    counts = {}
    for i in arr:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    
    trips = []
    arr = list(set(arr))
    for i in range(len(arr)-2):
        trips += trips_from(arr[i], doubles_from(arr[i+1], arr[i+2:]))
    
    summat = 0
    for t in trips:
        if testBeat(d, t):
            summat += 1  * counts[t[0]] * counts[t[1]] * counts[t[2]]
    return summat
    
def trips_from(n, arr):
    return [[n, a[0], a[1]] for a in arr]
      
def doubles_from(n, arr):
    if len(arr) > 1:
        return [[n, i] for i in arr] + doubles_from(arr[0], arr[1:])
    return [[n, i] for i in arr]
    
def testBeat(d, arr):
    # print(arr)
    return arr[0] < arr[1] < arr[2] and arr[1] - arr[0] == d and arr[2] - arr[1] == d


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
