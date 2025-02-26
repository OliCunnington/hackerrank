# Enter your code here. Read input from STDIN. Print output to STDOUT
m_s = int(input())
m = set(map(int, input().split()))
n_s = int(input())
n = set(map(int, input().split()))
for i in sorted(n.difference(m).union(m.difference(n))):
    print(i)