#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    cypher = "abcdefghijklmnopqrstuvwxyz"
    cYPHER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                result += cypher[(cypher.index(c)+k)%26]
            else:
                result += cYPHER[(cYPHER.index(c)+k)%26]
        else:
            result += c;
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
