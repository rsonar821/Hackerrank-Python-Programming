# 1. sWAP cASE

def swap_case(s):
    lst= []
    for i in s:
        if i == i.upper():
            lst.append(i.lower())
        elif i == i.lower():
            lst.append(i.upper())
        else:
            lst.append(i)

    st = ''
    j = st.join(lst)
    return j
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)