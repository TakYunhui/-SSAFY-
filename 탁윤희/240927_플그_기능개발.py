def solution(progresses, speeds):
    answer = []
    deploy = []
    # n번 작업이 배포되려면 앞에 있는 기능이 완성되어야 한다 !
    # => 각 작업 완성 일자를 구하는 게 의미가 있나 그럼?
    # 앞 작업 완성 여부를 확인해야 할듯 ?
    for i in range(len(speeds)):
        remain = (100 - progresses[i]) / speeds[i]
        if remain > int(remain):
            remain = int(remain) + 1
        else:
            remain = int(remain)
        deploy.append(remain)

    tmp = 1  # 첫 작업은 무조건 배포됨
    max_day = deploy[0]  # 첫 작업 배포 가능일
    for i in range(1, len(deploy)):
        # 이전 작업과 함께 배포 가능
        if deploy[i] <= max_day:
            tmp += 1
        else:
            answer.append(tmp)  # 현재까지 쌓인 기능 개수 추가
            tmp = 1  # 기능 개수 초기화
            max_day = deploy[i]  # 배포일 갱신
    answer.append(tmp)  # 마지막 배포 그룹 추가

    return answer