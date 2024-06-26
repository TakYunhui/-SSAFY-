# 9017 크로스 컨트리

# 리스트는 순위별 나열
# 각 팀 (1, 2, 3, ...) 의 등수(인덱스)들을 모아서, 합이 가장 적은 팀이 우승팀

import sys

sys.stdin = open('input.txt')

# 테스트케이스
T = int(input())


for _ in range(T):
    N = int(input())
    rank = list(map(int, input().split(' ')))
    teams = []
    points = []
    for i in range(N):
        points.append(i + 1)

    for i in range(N):
        # 새로운 팀이면
        if len(teams) < rank[i]:
            # rank[i] : 팀 이름, i : 점수 (인덱스)
            newTeam = [rank[i], 0, 1]   # 팀이름, 점수, 카운트
            teams.append(newTeam)
        # 체크했던 팀이면
        else:
            teams[rank[i]-1][2] += 1

    print(teams)
    for i in range(N):
        if rank[i] == 

    # pastPoint = 9999
    # for team in teams:
    #     if len(team[1]) < 6:
    #         pass
    #     else:
    #         currentPoint = sum(team[1][:4])
    #         # 현재 팀 점수가 직전 팀 점수보다 낮으면 결과 갱신
    #         if currentPoint < pastPoint:
    #             result = team[0]
    #     print(currentPoint)
    #     print(result)
    

    # print(result)



