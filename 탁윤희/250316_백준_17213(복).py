n = int(input())
m = int(input())
# 과일 종류 별 과일 훔침 경우의 수 저장 -> 이차원 리스트
# 종류: n, 훔치는 경우의 수: m
dp = [[0] * m for _ in range(n)]
dp[0] = [1] * m # 무조건 1개 종류는 훔치니까 첫번째 종류는 1개씩 넣음
for i in range(1, n): # 종류 1부터 n까지
    dp[i][i] = 1 # 과일 종류 i개 중 i 개 고르는 경우의 수 -> 1개 뿐인 것 넣기
    for j in range(i+1, m): # 종류별 훔침 개수 (2개부터 본다)
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
print(dp[-1][-1])
