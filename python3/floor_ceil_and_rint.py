import numpy

numpy.set_printoptions(legacy='1.13')

lst = numpy.array(list(map(float, input().split())))

print(numpy.floor(lst))
print(numpy.ceil(lst))
print(numpy.rint(lst))