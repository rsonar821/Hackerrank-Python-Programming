# 4. Concatenate

import numpy

n, m, p = map(int, input().strip().split())

a_arr = numpy.array([input().split() for i in range(n)], int)
b_arr = numpy.array([input().split() for j in range(m)], int)
print(numpy.concatenate((a_arr, b_arr), axis = 0))