# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = list(map(int, input().split()))

n = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res = 0
for i in n:
    if i in A:
        res += 1
    if i in B:
        res -= 1

print(res)