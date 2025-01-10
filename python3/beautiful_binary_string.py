#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    done = False
    counter = 0
    result = 0
    while not done:
        if(b[counter:counter+3] == "010"):
            counter += 3
            result += 1
        else:
            counter += 1
        if counter >= len(b):
            done = True
            break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
