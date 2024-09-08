# 실버 1. 줄어들지 않아
# 각 자리 수보다 그 왼쪽 자리수가 작거나 같을 때
# 숫자의 앞에 0이 있어도 된다
# n이 주어졌을 때, 줄어들지 않는 n 자리 수의 개수 구하기
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # 각 자리 숫자에 0부터 9까지가 들어갈 수 있으며, n까지 dp 값 필요
    dp = [[0] * 10 for _ in range(n+1)]

    for i in range(1, n+1):
        # 이전 자리 수의 총합이 첫번째 dp 값으로 들어가게 된다
        dp[i][0] = max(1, sum(dp[i-1]))
        # 현재 자리는 (현재 배열의 이전 자리 - 이전 배열의 이전 자리 값)
        for j in range(1, 10):
            dp[i][j] = max(1, dp[i][j-1] - dp[i-1][j-1])
    print(sum(dp[n]))