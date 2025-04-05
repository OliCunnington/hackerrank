# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
r = re.compile(input())
sub = r.search(s)
# print(r)
acum = 0
if sub:
    while sub: # and acum < len(s):
        print("("+ str(sub.start()) + ", " + str(sub.end() - 1) +")")
        acum = sub.start() + 1
        sub = r.search(s, acum)      
else:
    print("(-1, -1)")
