# 실버1. 1, 2, 3 더하기 5
import sys
input = sys.stdin.readline

# 1+2+3 인데 같은 숫자 연속 x
t = int(input())
dp = [[0 for _ in range(3)] for i in range(100001)]
# 1, 2, 3으로 끝나는 경우 저장
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # 1, 2, 3으로 끝나는 경우에 연속되지 않는 경우들 넣는다
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%1000000009
    dp[i][1] = (dp[i-2][2] + dp[i-2][0])%1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1])%1000000009


for j in range(t):
    n = int(input())
    # 마지막에도 나머지 연산
    print(sum(dp[n])%1000000009)
