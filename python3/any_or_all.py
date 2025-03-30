# Enter your code here. Read input from STDIN. Print output to STDOUT

input()

lst = list(map(int, input().split()))

pos_lst = [x >= 0 for x in lst]
palin_lst = [str(x) == str(x)[::-1] for x in lst]


print(all(pos_lst) and any(palin_lst))    