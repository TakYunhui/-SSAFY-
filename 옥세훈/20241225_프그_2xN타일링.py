def solution(n):
    
    dp = [0] * 600001
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    
    for i in range(2, n+1):
        dp[i+1] = (dp[i] + dp[i-1]) % 1000000007
    
    return dp[n-1]