# 실버 2. 과일 서리
n = int(input()) # 과일 종류
m = int(input()) # 과일 개수
# dp: 이차원배열 - 과일 종류에 따라 훔치는 경우의 수
dp = [[0] * m for _ in range(n)]
dp[0] = [1] * m # 무조건 1개의 종류는 써야하니 1 * m
for i in range(1, n):
    dp[i][i] = 1 # 과일 종류 2개 중 2개 고름 -> 1
    # 종류 별 과일 개수
    for j in range(i+1, m):
        # dp[i][j-1] : i종류에서 j-1개 훔치고 1개 더 훔쳐 맞추기
        # dp[i-1][j-1] : i종류에서 새로운 종류 사용해 훔치는 경우
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
print(dp[-1][-1])

