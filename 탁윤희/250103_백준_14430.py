# 실버 2. 자원 캐기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 2차원 배열 선언과 동시에 받기 - list를 다시 list[]로 감싸기!
area = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
# 오른쪽 또는 아래쪽 한 칸 이동 (0, 1) or (1, 0)
# 칸 별로 얻은 최대 자원 수 갱신?
# 2중 for문 써도 최대 900,00 정도

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = area[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
