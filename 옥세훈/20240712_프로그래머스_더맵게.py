import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] >= K:
            break
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break

        if len(scoville) > 1:
            num1 = heapq.heappop(scoville)
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (num1 + (num2 * 2)))
            answer += 1

    return answer

solution([1, 2, 3, 9, 10, 12],	7)