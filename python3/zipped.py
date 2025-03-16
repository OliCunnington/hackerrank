# Enter your code here. Read input from STDIN. Print output to STDOUT
x = list(map(int, input().split()))
res = []
for i in range(x[1]):
    if i == 0:
        res = list(map(float, input().split()))
    else:
        res = list(map(sum, list(zip(res, list(map(float, input().split()))))))
        
# print(res)

for i in range(x[0]):
    print(res[i]/x[1])