# 실버2. 리그오브레전설 (Small)
# 싸움 시간 n 동안 사용 가능한 스킬 조합 알기
# a : 1초 고정, b : m초 => a + b 로 만들 수 있는 초
n, m = map(int, input().split())
dp = [1] * (n+1) # i-1은 무조건 1이므로 1로 초기화
# i 초에 가능한 경우의 수
# 1. i-1초 + a
# 2. i >= m, i-m초에서 b 사용
# dp[i] = dp[i-1] + dp[i-m]
for i in range(m, n+1):
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007
print(dp[n])