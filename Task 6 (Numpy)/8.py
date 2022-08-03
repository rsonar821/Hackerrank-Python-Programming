# 8. Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')

a = list(map(float, input().strip().split()))
a_arr = numpy.array(a)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))