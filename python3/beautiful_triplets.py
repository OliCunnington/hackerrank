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

def testBeat(d, arr):
    return arr[0] < arr[1] < arr[2] and arr[1] - arr[0] == d and arr[2] - arr[1] == d

def beautifulTriplets(d, arr):
    counts = {}
    for i in arr:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    # Write your code here
    # make triplets, map test across
    # ascending list, < not <=
    # u_arr = set(arr)
    # print(u_arr)
    # need to make trips with just later numbers...
    # for i in range(len(arr)):
    # trips_from(arr[i], arr[i+1::]) ?
    # zip()
    # return len([1 for x in itertools.combinations(arr, 3) if testBeat(d, x)])
    # time out on large lists
    # need to only take elements later in list that != element...
    # can i do with set and multiply by... * count if count > 1 (??) 
    trips = list(itertools.combinations(set(arr), 3))
    # print(trips)
    # b_trips = [testBeat(d, t) for t in trips]
    summat = 0
    for t in trips:
        if testBeat(d, t):
            summat += 1 * counts[t[0]] * counts[t[1]] * counts[t[2]]
    # return b_trips.count(True)
    return summat
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
