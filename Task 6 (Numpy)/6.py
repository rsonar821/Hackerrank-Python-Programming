# 6. Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = tuple(map(int, input().strip().split()))

print(numpy.eye(n, m, k=0))