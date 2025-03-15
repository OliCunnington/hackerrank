# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range (int(input())):
    a = input()
    a = set(map(int, input().split()))
    b = input()
    b = set(map(int, input().split()))
    print(a <= b)