# Enter your code here. Read input from STDIN. Print output to STDOUT

first = input().split()
second = input().split()

res = [(int(x), int(y)) for x in first for y in second]
res_str = ""
for x in res:
    res_str += str(x) + " " 
print(res_str)
