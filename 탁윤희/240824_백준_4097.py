# 실버 2. 수익
# 연속된 일자 중 가장 수익이 많은 시기의 수익 출력
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    dp = [-10001] * (n+1)
    if n == 0:
        break
    p = list(int(input()) for _ in range(n))

    for i in range(n):
        dp[i] = max(dp[i], dp[i-1] + p[i], p[i])

    print(max(dp))