# 실버 2. 용돈 관리
import sys
input = sys.stdin.readline
# 돈 쓸 날 n, 인출 횟수 m (* 꼭 맞춰야 함)
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 용돈 찾기
# 시작: 하루에 쓸 최소 금액, 끝: 모든 금액의 총합 - 인출 1회로도 커버 가능해야 하기 때문
left, right = min(arr), sum(arr)
result = 0

while left <= right:
    mid = (left + right) // 2 # 용돈 금액
    now = mid
    draw = 1 # 인출 횟수

    for i in arr:
        # 쓰고 남은 현재 잔액이 써야할 돈보다 적다면
        # 다시 인출
        if now < i:
            now = mid
            draw += 1
        now -= i

    # 인출 횟수가 m 초과 (or) mid가 최댓값 보다 작다면 (인출해도 커버 x)
    if draw > m or mid < max(arr):
        # 용돈 금액을 늘린다
        left = mid + 1
    else:
        # 용돈 금액을 줄인다
        right = mid - 1
        # draw <= m이라면 조건에 맞으니 용돈 금액을 mid로 지정
        result = mid

print(result)



