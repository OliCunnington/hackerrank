#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    d = {ch : 0 for ch in string.ascii_lowercase}
    # print(d)
    for c in s.lower():
        if c != " ":
            d[c] += 1
    if min(d.values()) == 0:
        return "not pangram"
    return "pangram"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
