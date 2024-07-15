import math


def solution(progresses, speeds):
    answer = []
    length = len(speeds)
    ls_day = []
    for i in range(length):
        progresses[i] = 100 - progresses[i]
        ls_day.append(math.ceil(progresses[i] / speeds[i]))

    temp = ls_day[0]
    cnt = 1
    for i in range(1, length):
        # 뒤의 수가 더 클 경우
        if temp < ls_day[i]:
            answer.append(cnt)
            temp = ls_day[i]
            cnt = 1
            # 앞의 수가 더 클 경우
        else:
            cnt += 1

    answer.append(cnt)
    print(answer)
    return answer

solution([40, 20, 30, 20], [1, 1, 1, 1])