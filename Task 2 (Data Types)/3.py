main_lst = []
if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        lst = [name, score]
        main_lst.append(lst)
    
    temp_lst = []
    for i in range(len(main_lst)):
        temp_lst.append(main_lst[i][1])
    temp_lst2 = list(set(temp_lst))
    temp_lst2.sort()
    
    new_lst = []
    for i in range(len(main_lst)):
        if main_lst[i][1] == temp_lst2[1]:
            new_lst.append(main_lst[i][0])

    new_lst.sort()
    for i in new_lst:
        print(i)