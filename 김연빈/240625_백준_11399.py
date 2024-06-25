# ATM
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = dp[i] + arr[i]

print(sum(dp))
