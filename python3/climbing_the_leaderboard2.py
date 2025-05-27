#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # r = list(set(ranked))
    # r.sort(reverse=True)
    # r = dict(zip(ranked, map(lambda x: 0, ranked)))
    # res = []
    # keys = list(r.keys())
    # for x in player:
    #     i = 0
    #     if x in keys:
    #         i = keys.index(x)
    #     else:
    #         while i < len(r) and x < keys[i]:
    #             i += 1
    #     res.append(i + 1)
    scores = sorted(list(set(ranked)))
    index = 0
    res = []
    n = len(scores)
    for i in player:
        while (n > index and i >= scores[index]):
            index += 1
        res.append(n+1-index) 
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
