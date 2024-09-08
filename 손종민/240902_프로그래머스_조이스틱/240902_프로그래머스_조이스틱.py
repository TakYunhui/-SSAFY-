# 조이스틱
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# M보다 크면 

def solution(name):
    alphabet = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 
                'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    answer = -1
    for i in range(len(name)):
        if name[i] < 'M':
            answer += alphabet[name[i]]
        else:
            
            answer += (26 - alphabet[name[i]])
        
        if i == 0 and len(name) > 1 and name[i + 1] == 'A':
            answer -= 1
        answer += 1
    return answer


name = "JAZ"

print(solution(name))