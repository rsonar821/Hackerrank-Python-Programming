# 3. Transpose and Flatten

import numpy

n, m = map(int, input().strip().split())
ar = []
for i in range(n):
    row = list(map(int, input().strip().split()))
    ar.append(row)

np_ar = numpy.array(ar)
print(numpy.transpose(np_ar))
print(np_ar.flatten())
