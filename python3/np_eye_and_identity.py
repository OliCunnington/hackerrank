import numpy

numpy.set_printoptions(legacy='1.13')
nm = list(map(int, input().split()))
print(numpy.eye(nm[0], nm[1]))