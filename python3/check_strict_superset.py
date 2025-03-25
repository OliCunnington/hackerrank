# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
is_super = True

for i in range(int(input())):
    is_super = is_super and A >= set(map(int, input().split()))

print(is_super)