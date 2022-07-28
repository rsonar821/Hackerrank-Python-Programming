# 11. Set.discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    inst = input().split()
    if inst[0] == 'pop':
        s.pop()
    elif inst[0] == 'remove':
        s.remove(int(inst[1]))
    elif inst[0] == 'discard':
        s.discard(int(inst[1]))
        
sum = 0
for i in s:
  sum += i
print(sum)