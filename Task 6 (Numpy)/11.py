# 11. Mean, Var and Std

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().strip().split())

arr = []
for i in range(n):
    lst = list(map(int, input().strip().split()))
    arr.append(lst)

np_arr = numpy.array(arr)
print(numpy.mean(np_arr, axis=1))
print(numpy.var(np_arr, axis=0))
print(numpy.std(np_arr))