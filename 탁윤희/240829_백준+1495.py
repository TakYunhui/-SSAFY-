# 실버1. 기타리스트
import sys
input = sys.stdin.readline
# 곡 개수 n, 시작볼륨 5, 볼륨 최대 차이 m
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

# dp: 곡의 수 x 최대 볼륨 크기의 2차원 배열
# dp[i][j] == i번째 곡을 연주할 때 j 가능한지 나타냄
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1
# 현재 곡에서 볼륨 조절 여부 저장
for i in range(n):
    for j in range(m+1):
        # 현재 위치가 볼륨 조절 가능하다면
        # 현재 j값으로 볼륨 조절한 위치(값) 저장
        if dp[i][j] == 1:
            # M보다 큰 값으로 볼륨을 바꿀 수 없다
            if j + volumes[i] <= m:
                dp[i+1][j+volumes[i]] = 1
            # 0보다 작은 값으로 볼륨을 바꿀 수 없다
            if j - volumes[i] >= 0:
                dp[i+1][j-volumes[i]] = 1

result = -1
# 마지막 곡의 최대 볼륨 출력을 위해 역순으로 돌아봐서
# 볼륨 조절 가능한 위치면 그 값을 출력
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)