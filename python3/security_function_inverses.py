# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
outputs = input().split()
for i in range(n):
    outputs[i] = int(outputs[i])
for i in range (1,n+1):
    print(outputs.index(i)+1)
