# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

_in = input()
_out = ""
for key, group in groupby(_in):
    if len(_out) != 0:
        _out += " "
    _out += f"({len(list(group))}, {key})"
print(_out)