# 실버2. 가장 긴 감소하는 수열 - dp
n = int(input()) # 수열 a(list)의 크기
arr = list(map(int, input().split())) # 수열 a
dp = [1 for _ in range(n)] # 초기값: 1, 각 자리 부분 수열은 최소 1개임

# dp : dp[i]에 현재 i 자리의 숫자까지 왔을 때, 가능한 가장 긴 감소 수열 크기 넣기
for i in range(1, n):
    for j in range(i):
        if arr[j] > arr[i]: # 앞의 숫자가 더 크면 감소하는 수열이 됨
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))