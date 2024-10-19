from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    print(count)
    for k, v in count.items():
        if v > 1: answer += v * (v-1) / 2
    weights = list(set(weights))
    check = (3/4, 2/3, 1/2)
    for w in weights:
        for c in check:
            if w*c in weights:
                answer += count[w] * count[w*c]
    return answer


weights = [100,180,360,100,270]

print(solution(weights))