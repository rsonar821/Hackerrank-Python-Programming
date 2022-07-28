# 9. Symmetric Difference

if __name__ == '__main__'
x = int(input())
m = set(map(int, input().strip().split(' ')))
y = int(input())
n = set(map(int, input().strip().split(' ')))

lst = []
lst.extend(list(m.difference(n)))
lst.extend(list(n.difference(m)))
lst.sort()
for i in lst:
    print(i)