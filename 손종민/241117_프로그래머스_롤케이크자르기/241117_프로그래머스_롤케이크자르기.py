from collections import Counter

def solution(topping):
    answer = 0
    for i in range(len(topping)):
        a = Counter(topping[:i])
        b = Counter(topping[i:])
        if len(a) == len(b):
            answer += 1

    return answer

topping = [1, 2, 3, 1, 4]

print(solution(topping))