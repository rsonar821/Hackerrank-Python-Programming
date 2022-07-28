# 13. Set.intersection() Operation

n = int(input())
english_set = set(map(int, input().strip().split(' ')))
b = int(input())
french_set = set(map(int, input().strip().split(' ')))

total = english_set.intersection(french_set)
print(len(total))