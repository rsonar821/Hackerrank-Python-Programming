# 9. Designer Door Mat

n, m = map(int, input().strip().split())
for i in range(1, n, 2):
    print(str('.|.' * i).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n-2, -1, -2):
    print(str('.|.' * i).center(m, '-'))