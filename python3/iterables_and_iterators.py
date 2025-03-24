# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


n = int(input())
arr = input().split()
k = int(input())

comb = list(combinations(arr, k))
comb_a = [x for x in comb if 'a' in x]

print(len(comb_a)/len(comb))