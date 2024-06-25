def solution(participant, completion):
    dic = dict()
    answer = ''

    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for j in completion:
        dic[j] -= 1

    for k in dic.keys():
        if dic[k] > 0:
            answer = k

    return answer


solution(["leo", "kiki", "eden"], ["eden", "kiki"])