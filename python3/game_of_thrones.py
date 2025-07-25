#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    counts = {}
    for i in s:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1
    if len(s) % 2 == 0:
        for c in counts.values():
            if c % 2 != 0:
                return "NO"
        return "YES"
    else:
        odds = list(filter(lambda x: x%2 == 1, counts.values()))
        if len(odds) == 1:
            return "YES"
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
