import numpy

N = list(map(int, input().split()))
A = numpy.empty((N[0], N[1]), int)
B = numpy.empty((N[0], N[1]), int)

for i in range(N[0]):
    A[i] = list(map(int, input().split())) #, axis = 0)
for i in range(N[0]):
    B[i] = list(map(int, input().split())) #, axis = 0)

# Add ( + )
print(A + B)
# Subtract ( - )
print(A - B)
# Multiply ( * )
print(A * B)
# Integer Division ( / )
print(A // B)
# Mod ( % )
print(A % B)
# Power ( ** )
print(A ** B)