# 18. Check Subset

t = int(input())
for i in range(t):
    num_a = int(input())
    a = set(map(int, input().strip().split(' ')))
    num_b = int(input())
    b = set(map(int, input().strip().split(' ')))
    print(a.issubset(b))