# 실버 3. 진우의 달 여행
# 1. 지구 -> 달 방향 : (1, -1) | (1, 0) | (1, 1)
# 2. 어디서 시작하든 연료를 최대로 아끼며 달(가장 마지막 n)에 착륙 - m은 상관x
# 이전에 갔던 방향은 x
# 모든 경우의 수, 누적합 조합 구해서 최솟값 구하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# dp 테이블 : 3차원 리스트
# dp[i][j][k] : i번째 행, j번째 열, k방향으로 왔을 때의 최소 연료량
# k: 0 - 오른쪽 아래, 1 - 아래, 2 - 왼쪽 아래
# dp[0][j][k] : 초기값 0
# 나머지 dp : 무한대로 초기화하여 설정
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]
# dp 테이블 채우기
# i, j : 각각 행과 열
# 각 방향 이동 조건 (1. 인덱스 범위 2. 이전과 같은 방향x) 
for i in range(1,N+1):
    for j in range(M):
        # 오른쪽 아래로 가려면 현재 열 j가 마지막 열(m-1)보다 작아야 한다
        if j < M-1:
            # 0 - 오른쪽 아래 : 이전행의 왼쪽 아래나 아래 중 최소 값에 현재 소모량 더하기
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + matrix[i-1][j]
        # 왼쪽 아래로 가려면 현재 열 j가 0보다 커야 한다
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + matrix[i-1][j]
        # 아래로 가는 경우는 현재 j 범위에 상관없이 항상 유효
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i-1][j]

# 마지막 행에서 각 셀의 최소 연료 소모량 찾기
min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value, each)
print(min_value)