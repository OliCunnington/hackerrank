import numpy

n_m = list(map(int, input().split()))
arr = numpy.empty((n_m[0], n_m[1]))
for i in range(n_m[0]):
    arr[i] = list(map(int, input().split()))
    
print(int(numpy.prod(numpy.sum(arr, axis = 0))))