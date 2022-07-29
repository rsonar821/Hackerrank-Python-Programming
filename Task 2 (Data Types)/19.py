# 19. Check Strict Superset

a = set(map(int, input().strip().split(' ')))
n = int(input())
output = True
for i in range(n):
    temp_set = set(map(int, input().strip().split(' ')))
    if not temp_set.issubset(a):
        output = False
    if len(temp_set) >= len(a):
        output = False

print(output)