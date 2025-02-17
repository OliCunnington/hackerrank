# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import math
import cmath

initial_input = input()
split_in = []
both_neg = False
y_neg = False

if "+" in initial_input:
    split_in = initial_input.split("+")
elif initial_input.count("-") > 1:
    both_neg = True
    split_in = initial_input[1:].split("-")
else:
    y_neg = True
    split_in = initial_input.split("-")
    
x = int(split_in[0]) 
if both_neg: x *= -1
y = int(re.sub('[a-z]', '', split_in[1]))
if both_neg or y_neg: y *= -1

print(math.sqrt(x**2 + y**2))
print(cmath.phase(complex(x, y)))