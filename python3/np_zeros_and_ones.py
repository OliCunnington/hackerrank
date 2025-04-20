import numpy

n_m_i = tuple(map(int, input().split()))

print(numpy.zeros(n_m_i, dtype=int), numpy.ones(n_m_i, dtype=int), sep="\n")