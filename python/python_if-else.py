#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N%2 == 1:
    print("Weird")
elif N > 20:
    print("Not Weird")
elif N >= 6:
    print("Weird")
else:
    print("Not Weird")
