# 16. Set Mutations

size_a = int(input())
a = set(map(int, input().strip().split(' ')))
n = int(input())
for i in range(n):
    inst = input().strip().split(' ')
    temp_set = set(map(int, input().strip().split(' ')))
    if inst[0] == 'intersection_update':
        a.intersection_update(temp_set)
    elif inst[0] == 'update':
        a.update(temp_set)
    elif inst[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(temp_set)
    elif inst[0] == 'difference_update':
        a.difference_update(temp_set)
        
print(sum(list(a)))