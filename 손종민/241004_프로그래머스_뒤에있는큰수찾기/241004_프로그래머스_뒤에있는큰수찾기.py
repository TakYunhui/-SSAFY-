def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        is_big = False
        this_num = numbers[i]
        for j in range(i, len(numbers)):
            if numbers[j] > this_num:
                answer.append(numbers[j])
                is_big = True
                break
        if is_big == False:
            answer.append(-1)
    return answer



numbers = [9, 1, 5, 3, 6, 2]

print(solution(numbers))