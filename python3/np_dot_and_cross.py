import numpy

n = int(input())
a = numpy.empty((n,n))
b = numpy.empty((n,n))

for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    b[i] = list(map(int, input().split()))
    
print(numpy.matmul(a, b).astype(int))