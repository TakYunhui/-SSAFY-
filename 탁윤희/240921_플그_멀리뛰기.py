def solution(n):
    # dp 활용
    # dp[n]에 n칸일 때의 방법이 들어간다

    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 2001):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    answer = dp[n]
    return answer