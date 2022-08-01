# 14. Merge the Tools!

def merge_the_tools(string, k):
    lst = []
    len_lst = 0
    for i in string:
        len_lst += 1
        if i not in lst:
            lst.append(i)
        if len_lst == k:
            print (''.join(lst))
            lst = []
            len_lst = 0

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)