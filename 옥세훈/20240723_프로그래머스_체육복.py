
def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)

    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)

    if reserve:
        for i in reserve:
            if i-1 in lost:
                lost.remove(i-1)
            elif i+1 in lost:
                lost.remove(i+1)


    answer = n - len(lost)

    print(answer)
    return answer

solution(8, [3, 7], [2,4])
#  10, [1, 2, 3, 4, 5, 6], [1, 2, 3]