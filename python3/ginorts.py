# Enter your code here. Read input from STDIN. Print output to STDOUT
 
_in = input()
 
low = ''.join(c for c in _in if c.islower())
up = ''.join(c for c in _in if c.isupper())
num = ''.join(c for c in _in if c.isnumeric())
odd = ''.join(c for c in num if int(c) % 2 == 1)
even = ''.join(c for c in num if int(c) % 2 == 0)

res = ''.join(c for c in sorted(low)) + ''.join(c for c in sorted(up)) + ''.join(sorted(odd)) + ''.join(sorted(even))
print(res)