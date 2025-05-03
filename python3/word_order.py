# Enter your code here. Read input from STDIN. Print output to STDOUT

dic = {}
for i in range(int(input())):
    inp = input()
    if inp in dic.keys():
        dic[inp] += 1
    else:
        dic[inp] = 1

print(len(dic))
print(*[x for x in dic.values()])