def solution(progresses, speeds):
    # 현재 작업 진도 배열 progresses
    # 각 작업의 개발 속도 speeds
    # 각 기능의 개발 속도는 모두 다르지만
    # 앞에 있는 기능이 완료될 때 함께 배포된다
    answer = []
    # progresses 안에 남아있는 한
    while progresses:
        result = 0
        # 순회하면서
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

            
        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    result += 1
            answer.append(result)
    
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))