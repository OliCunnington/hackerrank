#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    sumat = 0
    for i in range (len(s)//2):
        if(s[i]!=s[len(s)-(i+1)]):
            sumat += abs(ord(s[i])-ord(s[len(s)-(i+1)]))
    return sumat
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
