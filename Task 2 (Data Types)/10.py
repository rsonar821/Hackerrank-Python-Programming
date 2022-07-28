# 10. Set.add()

if __name__ == '__main__':
    a = []
    for i in range(int(input())):
        x = input()
        a.append(x)
    
    b = set(a)
    print(len(b))