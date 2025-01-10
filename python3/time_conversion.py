#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if len(s) == 10:
        arr = s.split(':')
        return str(int(arr[0]) + 12)+":"+arr[1]+":"+arr[2][:2]
    return s
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
