# 실버 1. 팰린드롬 파티션
t = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2], dp[3] = 2, 2

# 점화식: dp[i] = dp[1] + dp[2] + ... + dp[i/2]
# 짝수일 때만 항이 늘어남
for i in range(4, 1001):
    if i % 2 == 0:
        dp[i] = dp[i-1] + dp[i//2] # 파이썬에서 "/"는 float 반환 하므로 // 나누기 이용
    else:
        dp[i] = dp[i-1]

for _ in range(t):
    n = int(input())
    print(dp[n])

