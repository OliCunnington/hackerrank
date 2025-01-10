#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
# isnt getting primes under x is a thing?
# 
# kek "get_next_prime"
# 2    3    5    7    11    13    17    19    23    29    31    37    41    43    47
# largest n 10^18, prod of above list is 6.148897825884914e+17
# next prime 53, prod 3.258915847719004e+19 which is > 10^18 (1e+18)...
# so largest possible answer is 15?
# list comp from this list of primes?
# ret len(primz)?

# i dont like this but i think primes make you do it...
# not like im going to crack that $$$ math problem...

def primeCount(n):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    prod_l = []
    while math.prod(prod_l) < n:
        prod_l.push(primes.popleft())
    return len(prod_l - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
