def solution(id_list, report, k):
    answer = []
    dic = dict()
    ans = dict()
    
    for i in id_list:
        dic[i] = []
        
    for i in report:
        a, b = i.split(" ")
        
        if b not in dic[a]:
            dic[a].append(b)
            ans[a] = 0
   
    # print(dic)
    for val in dic.values():
        if val:
            for i in val:
                if i not in ans:
                    ans[i] = 1
                else: 
                    ans[i] += 1

        
    for val in dic.values():
        cnt = 0
        if val:
            for i in val:
                if ans[i] >= k:
                    cnt += 1
                    
            answer.append(cnt)
        else:
            answer.append(0)
    return answer