#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # s = re.sub(" ", "", s)
    r = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))
    res = ""
    if r != c:
        r +=1
    for i in range(r):
        for j in range(c):
            ind = i + j*c
            # print(ind)
            if ind < len(s):  
                res += s[ind]
        res += " "
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
