from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    today = datetime.strptime(today, '%Y.%m.%d').date()
    
    dic = dict()
    for i in terms:
        term, m = i.split()
        dic[term] = int(m) * 28

    for i, j in enumerate(privacies):
        when, term = j.split(" ")
        when = datetime.strptime(when, '%Y.%m.%d').date()
        
        # 현재 - 과거 
        check = list(str(today - when).split(" "))
        hi = int(check[0]) // 28
        num = (hi * 28)-1
        print(num, dic[term])

        if num > dic[term]:
            answer.append(i+1)
    
    return answer