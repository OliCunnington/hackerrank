#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
nums = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", 
        "seventeen", "eighteen", "nineteen", 
        "twenty", "twenty one", "twenty two", 
        "twenty three", "twenty four", 
        "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine"
    ];
    
minutes = {
    15: "quarter",
    30: "half",
}

def get_word_from_num(n):
    # if quarter of half, ret that, else add " minutes"
    # only for minutes...
    if n == 15 or n == 30:
        return minutes[n]
    else:
        return str(nums[n]) + " minutes" if n != 1 else "one minute"


def timeInWords(h, m):
    if m == 0:
        return str(nums[h]) + " o' clock"
    elif m > 30:
        return get_word_from_num(60 - m) + " to " + str(nums[h+1])
    else:
        return get_word_from_num(m) + " past " + str(nums[h])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
