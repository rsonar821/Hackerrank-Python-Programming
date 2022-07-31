# 2. String Split and Join

def split_and_join(line):
    lst = line.split(' ')
    s = '-'
    final_str = s.join(lst)
    return final_str
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)