import re

vals = input().split()
poly = re.sub('x', vals[0], input())
print(int(vals[1]) == eval(poly))