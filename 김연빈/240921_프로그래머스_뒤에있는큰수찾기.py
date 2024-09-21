# 뒤에 있는 큰 수 찾기

# 뒤에 있는 숫자 중 크면서 가장 가까이 있는 수 찾기

# numbers = [2, 3, 3, 5]
numbers = [9, 1, 5, 3, 6, 2]

# 그냥 다 하면 시간초과 날 것 같은데..시간초과
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    max_num = max(numbers)
    for i in range(n-1):
        if (numbers[i]== max_num):
            answer[i] = -1
        else:
            for j in range(i+1, n):
                if numbers[i] < numbers[j]:
                    answer[i] = numbers[j]
                    break
            else:
                answer[i] = -1
    return answer

print(solution(numbers))