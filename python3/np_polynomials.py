import numpy

arr = input().split(" ")
x = int(input())
print(numpy.polyval([float(a) for a in arr], x))