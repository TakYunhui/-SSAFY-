# 실버1. 1, 2, 3 더하기 6
# 1, 2, 3 대칭 합으로 n만들기
import sys
input = sys.stdin.readline
t = int(input())
dp = [0] * 100001
# 대칭 - 끝자리 1+...+1, 2+...+2, 3+...+3
# => +2, +4, +6

dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6

for i in range(7, 100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009
for _ in range(t):
    n = int(input())
    print(dp[n])