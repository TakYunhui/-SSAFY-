# 실버 2. 민균이의 계략
# 순증가 순열 + 가장 많은 원소수
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    # 틀린 풀이: 현재 카드와 이전 카드만 비교해 정확한 최대 길이 증가 수열이 저장되지 않음
    # if cards[i-1] < cards[i]:
    #     dp[i] = dp[i-1] + 1
    # else:
    #     dp[i] = dp[0]
    tmp = 0
    for j in range(n-1, -1, -1): # 역순
        if cards[j] < cards[i]:
            tmp = max(tmp, dp[j])
        dp[i] = tmp + 1

print(max(dp))