# Enter your code here. Read input from STDIN. Print output to STDOUT

import os
import re
from itertools import permutations


def permutat(_input):
    res = [re.sub('[^A-Z]', '', x) for x in [str(r) for r in permutations(_input[0], int(_input[1]))]]
    res.sort()
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = permutat(input().split(" "))
    
    for r in result:
        fptr.write(str(r))
        fptr.write('\n')

    fptr.close()