import re

expressions = []
for _ in range(int(input())):
    try:
        re.compile(input())#compile as regex?
        expressions.append(True)#return true
    except re.error:
        expressions.append(False)
for _ in expressions:
    print(_)