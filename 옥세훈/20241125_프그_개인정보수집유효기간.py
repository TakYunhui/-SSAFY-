def dayday(date):
    y, m, d = map(int, date.split("."))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    answer = []
    today = dayday(today)
    
    dic = dict()
    for t in terms:
        type_, period = t.split()
        dic[type_] = int(period) * 28
        
    for idx, p in enumerate(privacies):
        num = idx + 1
        date, type_ = p.split()
        
        if dayday(date) + dic[type_] - 1 < today:
            answer.append(num)
    
    
    return answer