# 7. Array Mathematics

import numpy

n, m = map(int, input().strip().split())

for i in range(n):
    arr_a = numpy.array([list(map(int, input().split()))])

for j in range(n):
    arr_b = numpy.array([list(map(int, input().split()))])

print(arr_a + arr_b)
print(arr_a - arr_b)
print(arr_a * arr_b)
print(arr_a // arr_b)
print(arr_a % arr_b)
print(arr_a ** arr_b)