# 실버 1. 극장 좌석
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = list()
for _ in range(m):
    vips.append(int(input()))

# dp에는 좌석 i개에 앉을 수 있는 방법 수가 들어간다
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1
# 좌석 배치 경우의 수 -> 사람들이 자기 좌석 번호 바로 왼쪽 또는 오른쪽 이동
# => 피보나치 수열과 동일한 점화식
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
# 좌석을 구간으로 나누어 경우의 수 계산
result = 1
last_vip = 0 # 시작 구간의 처음 좌석 앞
for vip in vips:
    # 이전 vip 좌석과 현재 vip 좌석 사이 구간의 좌석 수
    between_vips = vip - last_vip - 1
    result *= dp[between_vips]
    last_vip = vip
# 마지막 vip 이후 좌석들 처리
between_vips = n - last_vip
result *= dp[between_vips]
print(result)