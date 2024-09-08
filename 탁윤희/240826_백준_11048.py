# 실버 2. 이동하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
dp = list(([0] * m) for _ in range(n))
# 각각의 방향으로 이동할 때의 누적 최대합을 구한다
for _ in range(n):
    maze.append(list(map(int, input().split())))

# 처음 위치를 maze 첫 위치로 초기화 - 하지 않으면 리스트 업데이트가 제대로 비교 갱신 안 됨
dp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        # 방향을 d 리스트로 정하지 않고 범위 별로 나누어 값을 구해준다
        # (1, 0)
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + maze[i][j])
        # (0, 1)
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1] + maze[i][j])
        # (1, 1)
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + maze[i][j])
print(dp[n-1][m-1])