import numpy

x = int(input())

arr = [list(map(float, input().split())) for i in range(x)]

print("{:.2}".format(numpy.linalg.det(arr)))