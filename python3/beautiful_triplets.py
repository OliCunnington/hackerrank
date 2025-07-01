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
    # make all doubles from arr[1:] where dou[1] - dou[0] == d and dou[1] > dou[0]
    # make all triples from filtered doubles 
    # return len([1 for n in arr for m in list(filter(lamda x -> x[0] > n, dou)) where m[0] - n == d)
    counts = {}
    for i in arr:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    
    trips = []
    arr = list(set(arr))
    ds = all_doulbes(d, arr)
    for i in range(len(arr)-2):
        trips += trips_from(d, arr[i], [_d for _d in ds if _d[0] > arr[i]])
    # print("trips: ", trips)
    
    summat = 0
    for t in trips:
        summat += 1  * counts[t[0]] * counts[t[1]] * counts[t[2]]
    return summat
    
def trips_from(d, n, arr):
    # print("trips_from: ", arr, "\t", n, "\t", d)
    trips = [[n, a[0], a[1]] for a in arr if a[0] - n == d]
    # print("trips_from res: ", trips, d, n, arr)
    return trips


def all_doulbes(d, arr):
    ds = []
    for i in range(len(arr)):
        for j in arr[i:]:
            if j - arr[i] == d:
                ds.append([arr[i], j]) 
    return(ds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
