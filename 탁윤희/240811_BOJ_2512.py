# 실버2. 예산
import sys
input = sys.stdin.readline

n = int(input()) # 지방 수
requests = list(map(int, input().split())) # 지방 별 예산 요청
m = int(input()) # 총 예산

# 국가 예산 총액 안에서 지방 예산 요청을 만족시키는 최댓값 예산 구하기
# left 값이 최소 값이 아니다 ( 100 100 100 100 100 , 10 같은 경우 0이 되버림)
left, right = 1, max(requests)
result = 0 # 먼저 선언해둬야 runtimeerror 안남

while left <= right:
    mid = (left + right) // 2
    total = 0

    for request in requests:
        if request <= mid:
            total += request
        else:
            total += mid

    # 예산 총액 이하라면 유효 상한액 늘리기
    # 현재 mid 값이 유효 상한액이므로 result가 된다
    if total <= m:
        result = mid
        left = mid + 1
    # 예산 총액 초과면 유효 상한액 줄이기
    else:
        right = mid - 1


print(result)