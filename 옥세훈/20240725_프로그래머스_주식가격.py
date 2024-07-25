def solution(prices):
    length = len(prices)
    answer = [0] * length

    for i in range(length):
        for j in range(i, length - 1):
            if prices[i] <= prices[j + 1]:
                answer[i] += 1
            else:
                break
    print(answer)
    return answer

solution([1, 2, 3, 2, 3])