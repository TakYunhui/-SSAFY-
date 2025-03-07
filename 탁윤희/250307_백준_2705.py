# 복습
import sys
input = sys.stdin.readline

t = int(input())

# 팰린드롬
# dp[i] = dp[i-1]+dp[i-2]+...+dp[i//2]
# 그런데? 짝수만 항이 추가된다
dp = [1] * (1001)
for i in range(1, 1001):
    if i % 2 == 0:
        dp[i] = dp[i-1] + dp[i//2]
    else:
        dp[i] = dp[i-1]

for _ in range(t):
    n = int(input())
    print(dp[n])