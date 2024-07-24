
def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    if reserve:
        for i in reserve:
            if i-1 in lost:
                lost.remove(i-1)
            elif i+1 in lost:
                lost.remove(i+1)


    answer = n - len(lost)

    print(answer)
    return answer

solution(10, [1, 2, 3, 4, 5, 6], [1, 2, 3])
#  10, [1, 2, 3, 4, 5, 6], [1, 2, 3]

