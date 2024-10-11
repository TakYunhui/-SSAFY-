from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    dict = defaultdict()
    for gyul in tangerine:
        if gyul in dict:
            dict[gyul] += 1
        else:
            dict[gyul] = 1
    print(dict)
    tmp = sorted(dict.values(), reverse=True)
    # list(tmp)
    print(tmp)
    for i in tmp:
        k -= i
        answer += 1
        if k <= 0:
            break
    print(answer)
    return answer

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

solution(k, tangerine)