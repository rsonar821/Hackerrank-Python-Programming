# 14. Set.difference() Operation

n = int(input())
english_set = set(map(int, input().strip().split(' ')))
b = int(input())
french_set = set(map(int, input().strip().split(' ')))

total = english_set.difference(french_set)
print(len(total))