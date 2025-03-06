n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    _in = input().split()
    if len(_in) > 1:
        exec("s." + _in[0] + "(" + _in[1] + ")")
    else:
        exec("s." + _in[0] + "()")
    
    
print(sum(s))