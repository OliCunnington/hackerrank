# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())
list = input().split()
bij = True
for i in range (x):
    for j in range (x):
        if i == j:
            pass
        elif list[i] == list[j]:
            bij = False
if bij:
    print("YES")
else:
    print("NO")
            
