# 실버1. 1, 2, 3 더하기 7
import sys
input = sys.stdin.readline
t = int(input())
# n을 1, 2, 3의 합으로 나타내는 방법의 수
# 이때 위 1, 2, 3을 m개 사용
# -> 1부터 n까지를 1부터 n개까지 써서 만드는 경우의 수..
# 2중리스트로 구하기
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4, 1001):
    for j in range(2, 1001):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % 1000000009

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])