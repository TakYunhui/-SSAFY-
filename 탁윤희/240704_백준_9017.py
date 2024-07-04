# 실버 3 : 크로스컨트리
# 우승팀: 6명 모두 완주, 상위 4명 주자의 점수 합산
# 동점 - 다섯 번째 주자가 가장 빨리 들어온 팀이 우승
# list 안 팀 번호를 dict key + list 내 index를 value로 저장
# 이때, value의 index는 list 내에 추가되는 형태로 작성
# 팀 인원 value list length로 구해서 6명이 안 되면 제외
# list 기반으로 점수 계산
t = int(input())
for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))

    manage = {}
    for j in range(n):
        if team[j] not in manage:
            # 팀 명수, 선수들 점수리스트, 점수합계
            manage[team[j]] = [1, [], 0]
        else:
            manage[team[j]][0] += 1

    # 선수들의 수가 조건에 맞지 않는 팀을 우선걸러낸다
    contain = set(k for k, v in manage.items() if v[0] < 6)

    grade = 1
    for j in range(n):
        # 점수계산에서 제외해야 하는 선수가 아니라면
        if team[j] not in contain:
            manage[team[j]][1].append(grade)
            # 점수를 더하는건 상위 4명의 점수까지만 합산
            if len(manage[team[j]][1]) <= 4:
                manage[team[j]][2] += grade
            grade += 1

    answer = []
    for k, v in manage.items():
        if len(v[1]) != 0 and v[2] != 0:
            answer.append([k, v[1][4], v[2]])

    a = sorted(answer, key=lambda x: (x[2], x[1]))
    print(a[0][0])