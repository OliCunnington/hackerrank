import numpy

n_m = list(map(int, input().split()))
arr = numpy.empty((n_m[0], n_m[1]), dtype = int)
for i in range(n_m[0]):
    arr[i] = list(map(int, input().split()))
    
print(numpy.transpose(arr))
print(arr.flatten())
