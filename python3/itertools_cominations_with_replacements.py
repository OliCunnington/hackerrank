# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
import re

_in = input().split()
for i in list(combinations_with_replacement(sorted(_in[0]), int(_in[1]))):
    print(re.sub('[^A-Z]', '', str(i)))