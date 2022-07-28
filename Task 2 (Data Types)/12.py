# 12. Set.union() Operation

n = int(input())
english_set = set(map(int, input().strip().split(' ')))
b = int(input())
french_set = set(map(int, input().strip().split(' ')))

total = english_set.union(french_set)
print(len(total))