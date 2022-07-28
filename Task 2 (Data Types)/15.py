# 15. Set.symmetric_difference() Operation

n = int(input())
english_set = set(map(int, input().strip().split(' ')))
b = int(input())
french_set = set(map(int, input().strip().split(' ')))

total = english_set.symmetric_difference(french_set)
print(len(total))