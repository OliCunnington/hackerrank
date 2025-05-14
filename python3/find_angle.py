# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


AB = int(input())
BC = int(input())
MBC = round(math.atan(AB/BC) * 180/math.pi)
print(MBC, chr(176), sep="")
