# 실버 1. 보석 상자
# m가지 색상의 보석을 n명에게 나눠주기
# 보석을 못 받는 학생이 있어도 된다, 보석 받는 애들은 같은 색상만 받는다
# 한 아이가 너무 많은 보석을 가지면 질투심 생김
# 질투심: 많은 보석을 가진 학생의 보석 수
# 질투심이 최소 -> 질투심이 이분탐색으로 구할 result
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = list(int(input()) for _ in range(m))

left, right = 1, max(jewels)
result = 0

while left <= right:
    mid = (left + right) // 2
    # 보석을 최대 mid로 나눌 때, 몇 명의 학생이 나오는지 계산할 total
    total = 0

    for jewel in jewels:
        # 올림 연산으로 계산
        total += (jewel + mid - 1) // mid

    if total <= n: # 학생 수 조건에 맞추기
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)