# 5. Find a String

def count_substring(string, sub_string):
    l = len(sub_string)
    lst = []
    for i in range(len(string)):
        lst.append(string[i:i+l])
        
    counter = 0
    for i in lst:
        if sub_string == i:
            counter += 1
          
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)