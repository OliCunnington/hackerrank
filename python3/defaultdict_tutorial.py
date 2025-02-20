# Enter your code here. Read input from STDIN. Print output to STDOUT

inp = input().split()
n = int(inp[0])
m = int(inp[1])

ns = {}
for a in range(n):
    character = input()
    if character in ns.keys():
        ns[character].append(a+1)
    else:
        ns[character] = [a+1]

for a in range(m):
    character = input()
    if character in ns.keys():
        res = ""
        for c in ns[character]:
            res += str(c) + " "
        print(res)
    else:
        print("-1")