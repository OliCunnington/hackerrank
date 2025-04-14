# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    c = input().split()
    if len(c) > 1 and c[1] != "{":
        for k in c:
        # if k[0] == "#":
        #     if len(c) == 4 or len(c) == 7:
            if re.search(r"#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})[;,)]?", k):
                print(re.sub(r"^.*:", "", re.sub(r"[,;)]", "", k)))
