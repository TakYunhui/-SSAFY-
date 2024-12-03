def check(ls):
    lss = []
    for i in ls:
        if i in ["[","{","("]:
            lss.append(i)
        else:
            if lss and i ==  "]" and lss[-1] == "[":
                lss.pop()
            elif lss and i ==  ")" and lss[-1] == "(":
                lss.pop()
            elif lss and i ==  "}" and lss[-1] == "{":
                lss.pop()
            else:
                lss.append(i)
                
    if len(lss) > 0:
        return 0
    
    return 1

def solution(s):
    answer = 0
    x = len(s)
    ls = list(s)
    
    for i in range(x):
        c = ls.pop(0)
        ls.append(c)
        
        answer += check(ls)
    
    return answer