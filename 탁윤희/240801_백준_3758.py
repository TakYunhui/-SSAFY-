# 실버 2. KCPC
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    teams = [([0] * k) for i in range(n)]
    cnts = [0] * n
    logs = [0] * n

    # 각 팀의 총합, 제출 횟수, 마지막 로그 제출 구하기
    for x in range(m):
        i, j, s = map(int, input().split())
        if teams[i-1][j-1] < s:
            teams[i-1][j-1] = s
        cnts[i-1] += 1
        logs[i-1] = x

    ranks = []
    # 위의 정보에 팀 번호 추가
    for i in range(n):
        ranks.append([sum(teams[i]), cnts[i], logs[i], i+1])
    # 조건에 따른 정렬 - 점수 큰 순 > 제출 횟수 적은 순 > 로그가 작은 순
    ranks.sort(key=lambda x: (-x[0], x[1], x[2]))

    for i in range(n):
        if ranks[i][3] == t:
            print(i+1)