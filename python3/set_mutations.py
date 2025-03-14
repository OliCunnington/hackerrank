# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
a = set(map(int, input().split()))
n = []
for i in range(int(input())):
    n.append(tuple((input().split()[0], set(map(int, input().split())))))
    
for i in n:
    exec("a." + i[0] + "(" + str(i[1]) + ")")

print(sum(a))