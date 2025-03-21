# 실버2. 병사 배치하기
# 특정 위치 병사를 없애서 전투력 높은 순으로 내림차순 정렬
# 최대 병사 수 남기기
import sys
input = sys.stdin.readline

n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * n # 각 병사가 자기 자신만 포함하는 LDS 가짐
# i번째 병사가 자기를 포함해서 만들 수 있는 최대 길이 구하는 반복문
for i in range(n):
    for j in range(i):
        if soldiers[i] < soldiers[j]: # i 이전 병사의 전투력이 더 크면(내림차순)
            dp[i] = max(dp[i], dp[j] + 1)
# 열외되는 병사 수 : n - 최대 병사 수
print(n - max(dp))