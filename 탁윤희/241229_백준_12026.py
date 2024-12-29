# 실버1. BOJ 거리
# B, O, J 순서대로 이동 가능
# K칸 점프: k * k 에너지 소요
# boj 순서가 맞으면 이동 가능함, 최소 에너지 저장해둠
n = int(input())
word = list(input())
# dp 에 최소 에너지 저장해야하니 큰 수를 저장
dp = [1e9] * (n+1)
dp[0] = 0 # 항상 B로 시작

# 2차원 반복문을 통해 현재 글자~n까지의 글자들 알아내어 조건식에 씀
for i in range(n):
    for j in range(i+1, n): # i+1부터 n까지의 다음 글자들 확인
        # BOJ 순서가 맞는 지 확인
        # 순서가 맞다면 기존 dp[j]와 dp[i] + k*k 값 대소 비교해 넣기
        if word[i] == 'B' and word[j] == 'O':
            dp[j] = min(dp[j], dp[i] + (j-i) ** 2)
        if word[i] == 'O' and word[j] == 'J':
            dp[j] = min(dp[j], dp[i] + (j-i) ** 2)
        if word[i] == 'J' and word[j] == 'B':
            dp[j] = min(dp[j], dp[i] + (j-i) ** 2)

if dp[n-1] == 1e9:
    print(-1)
else:
    print(dp[n-1])