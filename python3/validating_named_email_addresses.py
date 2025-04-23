# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

for i in range(int(input())):
    e = email.utils.parseaddr(input())
    if e != ('', '') and re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', e[1]):
        print(email.utils.formataddr(e))