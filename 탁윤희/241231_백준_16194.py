# 실버1. 카드 구매하기 2
import sys
input = sys.stdin.readline

n = int(input())
amounts = list(map(int, input().split()))
# dp[i]에 i 개를 사는 최솟값 저장
dp = [1e9] * (n+1)
# 0개 구매 비용: 0
dp[0] = 0
for i in range(1, n+1): # 카드 i 개 구매
    for j in range(1, i+1): # 카드팩 j개 사용
        # amounts에는 1번 값이 0번 인덱스부터 저장되므로 -1 해줌
        # i - j + j - 1 == n 이 되는 경우의 수들
        dp[i] = min(dp[i], dp[i-j] + amounts[j-1])

print(dp[n])