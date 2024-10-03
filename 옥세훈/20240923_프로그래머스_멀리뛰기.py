def solution(n):
    answer = 0
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    if n <= 3:
        return dp[n]

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[0:n + 1])
    answer = dp[n] % 1234567
    return answer