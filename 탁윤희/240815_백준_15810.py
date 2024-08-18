# 실버 2. 풍선 공장
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balloons = list(map(int, input().split()))

# 풍선 m개를 만드는 최소 시간 구하기
left, right = 1, max(balloons) * m
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    # mid분동안 스태프들이 부는 풍선 개수 구하기
    for balloon in balloons:
        total += mid // balloon

    # m 이상이면 시간을 줄인다
    if total >= m:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)