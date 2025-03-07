# 복습.
n, m = map(int, input().split())
dp = [1] * (10001)
# 반복문: m부터 시작하는 이유 - m이하의 수들은 dp[i-m]이 존재하지 않아 갱신하면 안되기 때문
# -> 1부터 넣으면 dp[i-m]에 접근 시도하며 잘못된 값이 들어감
for i in range(m, n + 1):
    # 두 가지 경우: 1초 남기거나 m초 남기기
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007
print(dp[n])