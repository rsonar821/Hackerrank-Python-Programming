# 4. Mutations

def mutate_string(string, position, character):
    lst = []
    for i in range(len(string)):
        if i==position:
            lst.append(character)
        else:
            lst.append(string[i])
            
    s = ''
    final_str = s.join(lst)
    
    return final_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)