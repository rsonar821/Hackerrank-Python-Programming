# 13. The Minion Game

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowel_list:
            stuart_score += (len(string))-i
        else :
            kevin_score += (len(string))-i
    
    if stuart_score > kevin_score:
        print("Kevin", stuart_score)
    elif stuart_score < kevin_score:
        print("Stuart", kevin_score)
    elif kevin_score == stuart_score:
        print("Draw")
    else :
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)