# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools


k_m = list(map(int, input().split()))
ns = []
for _ in range(k_m[0]):
    ns.append([x*x for x in list(map(int, input().split()[1:]))])
s = [sum(x) % k_m[1] for x in itertools.product(*ns)]
    
print(max(s))