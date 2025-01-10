# Enter your code here. Read input from STDIN. Print output to STDOUT

string = input()

res = -1
for c in string:
    if c.isalnum() and c+c in string:
        res = c
        break

print(res)