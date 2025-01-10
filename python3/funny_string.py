#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    forward = [ord(x) for x in s]
    backwards = [ord(x) for x in s[::-1]]
    for x in range(len(s)-1):
        forward[x] = abs(forward[x] - forward[x+1])
        backwards[x] = abs(backwards[x] - backwards[x+1])
        if(forward[x] != backwards[x]):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
