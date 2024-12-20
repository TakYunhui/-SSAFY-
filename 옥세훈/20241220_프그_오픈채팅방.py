def solution(record):
    answer = []
    dic = dict()
    
    chat = []
    for i in record:
        ls = i.split(" ")
        
        if len(ls) > 2:
            dic[ls[1]] = ls[2]
            
    for i in record:
        check = i.split(" ")
        
        if check[0] == "Enter":
            answer.append(f"{dic[check[1]]}님이 들어왔습니다.")
        elif check[0] == "Leave":
            answer.append(f"{dic[check[1]]}님이 나갔습니다.")

            
            
    return answer


