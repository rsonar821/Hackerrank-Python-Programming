# 17. The Captain's Room

k = int(input())
a = list(map(int, input().split()))

set_a = set()
set_b = set()

for i in a:
    if i in set_a:
        set_b.add(i)
    else:
        set_a.add(i)
print(set_a.difference(set_b).pop())