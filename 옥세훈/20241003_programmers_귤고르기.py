def solution(k, tangerine):
    answer = 0
    dic = dict()

    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for _, cnt in sorted_dic:
        if k <= 0:
            break
        answer += 1
        k -= cnt

    return answer