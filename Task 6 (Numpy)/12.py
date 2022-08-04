# 12. Dot and Cross

import numpy

n = int(input())

for i in range(n):
    a = numpy.array([input().split()], int)
    b = numpy.array([input().split()], int)

print(numpy.dot(a, b))