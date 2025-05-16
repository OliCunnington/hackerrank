#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
# 8   1   6
# 3   5   7
# 4   9   2
magics = [
            [[8,1,6],[3,5,7],[4,9,2]],
            [[6,1,8],[7,5,3],[2,9,4]],
            [[4,9,2],[3,5,7],[8,1,6]],
            [[2,9,4],[7,5,3],[6,1,8]],
            [[8,3,4],[1,5,9],[6,7,2]],
            [[4,3,8],[9,5,1],[2,7,6]],
            [[6,7,2],[1,5,9],[8,3,4]],
            [[2,7,6],[9,5,1],[4,3,8]]
    ]

def sub_mat(a, b):
    res = [[],[],[]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            res[i].append(abs(a[i][j]-b[i][j]))
    return res

def formingMagicSquare(s):
    # Write your code here
    unsumed_cost = [sub_mat(s, x) for x in magics]
    summed_cost = [sum(list(map(sum, x))) for x in unsumed_cost]
    return min(summed_cost)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
