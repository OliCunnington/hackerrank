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
    for i in range(len(arr)-2):
        trips += trips_from(d, arr[i], doubles_from(d, arr[i+1], arr[i+2:]))
    print("trips: ", trips)
    
    summat = 0
    for t in trips:
        summat += 1  * counts[t[0]] * counts[t[1]] * counts[t[2]]
    return summat
    
def trips_from(d, n, arr):
    print("trips_from: ", arr, "\t", n, "\t", d)
    trips = [[n, a[0], a[1]] for a in arr if a[0] - n == d]
    print("trips_from res: ", trips, d, n, arr)
    return trips
      
def doubles_from(d, n, arr):
    # if len(arr) > 1:
    #     #probably hitting recursion depth...
    #     return [[n, i] for i in arr if i - n == d] + doubles_from(d, arr[0], arr[1:])
    # return [[n, i] for i in arr if i - n == d]
    doubles = []
    for j in range(len(arr)-1):
        doubles += [[n, i] for i in arr[j:] if i - n == d]
    print("doubles_from res: ", doubles, d, n, arr)
    return doubles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
