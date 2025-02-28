from itertools import combinations
import re


_in = input().split()
combs = []

for i in range(1, int(_in[1]) + 1):
    combs += combinations(sorted(_in[0]), i)

for s in combs:
    print(re.sub('[^A-Z]', '', str(s)))