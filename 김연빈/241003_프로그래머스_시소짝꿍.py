def solution(weights):
    answer = 0
    before_answer = 0
    n = len(weights)
    weights.sort()
    if weights[0] == weights[-1]:
        answer = n*(n-1)//2
        return answer
    for i in range(n-1):
        if i!=0 and weights[i]==weights[i-1]:
            if (before_answer > 0):
                before_answer -= 1
            answer += before_answer
            # print(i)
        else:
            before_answer = 0
            for j in range(i+1, n):
                if weights[i] == weights[j]:
                    answer += 1
                    before_answer += 1
                    # print(i, j)
                elif weights[i]*2 == weights[j]:
                    answer += 1
                    before_answer += 1
                    # print(i, j)
                elif weights[i]*3 == weights[j]*2:
                    answer += 1
                    before_answer += 1
                    # print(i, j)
                elif weights[i]*4 == weights[j]*3:
                    answer += 1
                    before_answer += 1
                    # print(i, j)
        # print(before_answer)
        # print('ans', answer)
    return answer