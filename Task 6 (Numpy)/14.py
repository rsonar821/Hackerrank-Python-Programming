# 14. Polynomials

import numpy

lst = list(map(float, input().split()))
p = numpy.array(lst)
x = int(input())
print(numpy.polyval(p, x))