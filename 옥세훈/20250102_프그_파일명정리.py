def solution(files):
    answer = []
    ls = []
    
    for i in files:
        head = ''
        num = ''
        tail = ''
    
        
        for j in range(len(i)):
            if i[j].isdigit():
                num += i[j]
            elif not num:
                head += i[j]
            else:
                tail += i[j:]
                break
                
        print([head, num, tail])
        ls.append((head, num, tail))     

        
    ls.sort(key=lambda x : (x[0].upper(), int(x[1])))
    
    for i in ls:
        answer.append(''.join(i))
    
    # print(answer)
    return answer
