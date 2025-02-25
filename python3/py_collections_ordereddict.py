# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
import re


od = OrderedDict()
for i in range(int(input())):
    _inp = input()
    inp = []
    inp.append(re.sub('[0-9]', '', _inp).strip())
    inp.append(int(re.sub('[a-z,A-Z]', '', _inp)))
    if inp[0] in od.keys():
        od[inp[0]] += int(inp[1])
    else:
        od[inp[0]] = int(inp[1])

for key in od.keys():
    print(key, od[key])