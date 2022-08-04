# 10. Min and Max

import numpy

n, m = map(int, input().strip().split())

arr = []
for i in range(n):
    lst = list(map(int, input().strip().split()))
    arr.append(lst)

np_arr = numpy.array(arr)
new_arr = numpy.min(np_arr, axis=1)
print(numpy.max(new_arr))