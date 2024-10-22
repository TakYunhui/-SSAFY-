# 현재 인덱스보다 뒤의 요소들을 비교하면서
# 0.5배거나, 0.75베거나, 같거나, 1.5배거나, 2배일 경우에
# 기록하기

def solution(weights):
    answer = 0
    for i in range(len(weights)):
        # 현재 인덱스 다음 인덱스부터 하나씩 비교하기
        for j in range(i + 1, len(weights)):
            if weights[i] == weights[j] or weights[i] * 0.5 == weights[j]or weights[i] * 0.75  == weights[j]or weights[i] * 1.5  == weights[j]or weights[i] * 2 == weights[j]:
                # print('현재 요소', weights[i])
                # print('비교 요소', weights[j])
                answer += 1
    return answer

weights = [100,180,360,100,270]

print(solution(weights))