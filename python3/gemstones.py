#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    result = {}
    for a in arr:
        for c in list(set(a)):
            try:
               result[str(c)] += 1
            except:
                result[str(c)] = 1
    res = 0
    print (result)
    for r in result.values():
        if(r == len(arr)):
            res+=1
    return res        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
