# [0] 0
# [3, 4] 2
# [1, 2, 3, 5, 6, 7, 10, 11] 5
# [3, 5, 11, 6, 1, 5, 3, 3, 1, 41] 5
# [1, 11, 111, 1111] 3


def solution(citations):
    answer = 0

    citations.sort()
    print(citations)
    if citations.count(citations[0]) == len(citations):
        return len(citations)

    for i in range(len(citations)):
        cnt = 0
        for j in range(i, len(citations)):
            if citations[i] < citations[j]:
                cnt += 1

        if cnt >= citations[i]:
            answer = cnt

    print(answer)
    return answer

solution([4,4,4])