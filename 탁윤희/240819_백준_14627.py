# 실버 2. 파닭파닭
import sys
input = sys.stdin.readline
# 시장에서 사온 파의 개수, 주문 받은 파닭 수
s, c = map(int, input().split())
arr = list(int(input()) for _ in range(s))
# 각 파닭에 같은 양의 파를 최대한 많이 넣는다, 파의 종류는 1개만
# 파닭 수에 맞춰 최대 길이 x를 구한다
# x를 구하고 각 파에서 x를 뺀 값의 합(나머지 합산)을 result로 출력
left, right = 1, max(arr)
x = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for i in arr:
        cnt += i // mid

    # mid로 나눈 파닭 개수가 요구 이상이면 파 길이 더 늘리기 + x가 파 길이로 채택 가능
    if cnt >= c:
        x = mid
        left = mid + 1
    else:
        right = mid - 1

# 파닭을 만들고 남은 파의 양 계산
used_pieces = sum(i // x for i in arr)
remaining_pieces = sum(i % x for i in arr)

# c개 이상의 파닭을 만들고 남은 파의 길이
result = remaining_pieces + (used_pieces - c) * x

print(result)