import numpy


nmp = list(map(int, input().split()))
_n =[]
_m =[]
for i in range (nmp[0]):
    _n.append(list(map(int, input().split())))

for i in range (nmp[1]):
    _m.append(list(map(int, input().split())))

print(numpy.concatenate((numpy.array(_n), numpy.array(_m))))