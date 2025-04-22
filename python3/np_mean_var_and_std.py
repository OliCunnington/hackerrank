import numpy

n_m = tuple(map(int, input().split()))

arr = numpy.empty(n_m)

for i in range(n_m[0]):
    arr[i] = list(map(int, input().split()))
    
    
print(numpy.mean(arr, axis=1), numpy.var(arr, axis=0), sep="\n")
std_arr = numpy.std(arr)
print( "{:.12}".format(std_arr)) if std_arr > 1 else print( "{:.11}".format(std_arr))