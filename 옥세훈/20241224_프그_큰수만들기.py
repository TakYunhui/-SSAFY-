def solution(number, k):
    answer = []
    
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            # print(answer, i)
            answer.pop()
            k -= 1
        answer.append(i)
        print(answer)
            
    return ''.join(answer[:len(answer)-k])