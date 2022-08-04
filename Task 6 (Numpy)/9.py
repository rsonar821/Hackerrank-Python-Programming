# 9. Sum and Prod

import numpy

n, m = map(int, input().strip().split())

arr = []
for i in range(n):
    lst = list(map(int, input().strip().split()))
    arr.append(lst)

np_arr = numpy.array(arr)

new_arr = numpy.sum(np_arr, axis=0)
print(numpy.product(new_arr))