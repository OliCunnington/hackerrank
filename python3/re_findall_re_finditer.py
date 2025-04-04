# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


val = input()
res = re.findall(r"(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])[aeiouAEIOU]{2,}(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])", val)
if len(res) > 0:
    for s in res:
        print(s)
else:
    print(-1)