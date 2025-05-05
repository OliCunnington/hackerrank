#!/bin/python3

import math
import os
import random
import re
import sys
from functools import cmp_to_key



if __name__ == '__main__':
    s = input()
    d = {}
    for c in s:
        if c not in d.keys():
            d[c] = s.count(c)
    arr = [x for x in d.items()]
    s_a = sorted(arr, key=cmp_to_key(lambda x, y: ord(y[0]) - ord(x[0]) if x[1] == y[1] else x[1] - y[1]), reverse=True)
    
    for i in range(3):
        print(*s_a[i])