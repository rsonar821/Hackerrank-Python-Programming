# 8. No Idea!

if __name__ == '__main__':
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    lst = list(map(int, input().strip().split(' ')))

    if len(lst) == n:
        pass
    else:
        print('break')

    a = set(map(int, input().strip().split(' ')))
    b = set(map(int, input().strip().split(' ')))

    if len(a) == m and len(b) == m:
        pass
    else:
        print('break')
        
    for i in lst:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
    
    print(happiness)