#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    arr = s.split(':')
    if s[-2:]=="PM":
        if arr[0] == '12':
            return s[:-2:]
        else:
            return str(int(arr[0]) + 12)+":"+arr[1]+":"+arr[2][:2]
    else:
        if arr[0] == '12':
            return "00:"+arr[1]+":"+arr[2][:2]
        else:
            return s[:-2:]
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
