#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    if len(s) == 1 or s[0] == "0" or (len(s) == 2 and int(s[0])+1 != int(s[1])):
        print("NO")
        return
    num = [int(s[0])]
    i = 1
    while i < len(s):
        if s.startswith(str(num[-1]+1), i):
            num += [num[-1]+1]
            i += len(str(num[-1]))
        else:
            if i > math.ceil(len(s)/2):
                print("NO")
                return
            num = [int(str(num[0]) + s[i])]
            i = len(str(num[0]))
    print("YES " + str(num[0]))


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
