# 실버2. 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * (1000001) # n <= 1,000,000 이므로 백만+1을 max 배열
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for _ in range(t):
    print(dp[int(input())])