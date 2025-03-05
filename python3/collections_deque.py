from collections import deque

d = deque()

for i in range(int(input())):
    _in = input().split()
    if len(_in) > 1:
        exec("d." + _in[0]+"(" + _in[1] + ")")
    else:
        exec("d." + _in[0] + "()")

print(' '.join(str(x) for x in d))