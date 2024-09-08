# 실버 1. 점프
import sys
input = sys.stdin.readline

n = int(input())
board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

# dp[i][j] : (i,j)까지 이동할 수 있는 경로의 개수
for i in range(n):
    for j in range(n):
        distance = board[i][j]
        # 현재 위치 값이 0이면 종착지
        if distance == 0:
            continue # 루프를 진행하지 않고 멈춤 => 현재 경로에서 +0 이동하지 않게 막ㅇ므
        # 이동될 dp 칸에 현재 dp 칸의 경로 수를 더해준다
        # 오른쪽 이동
        if i + distance < n:
            dp[i+distance][j] += dp[i][j]
        # 아래쪽 이동
        if j + distance < n:
            dp[i][j+distance] += dp[i][j]

print(dp[n-1][n-1])