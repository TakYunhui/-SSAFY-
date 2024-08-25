# 실버 2. 타일링
# 2xn의 직사각형을 2x1, 2x2 타일로 채우기
# dp[i-1] + 2x1 - 여기에 2x1 (두개 세로 포함)
# dp[i-2] + 2x2 or dp[i-2] + 2x1 (두개 가로)
dp = [0 for _ in range(251)]
dp[0] = 1
dp[1] = 1
dp[2] = 3
while True:
    try:
        n = int(input())
        for i in range(3, n+1):
            dp[i] = dp[i-1] + 2 * dp[i-2]
        print(dp[n])

    except:
        break