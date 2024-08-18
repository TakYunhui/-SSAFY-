# 실버 2. 이상한 술집
# 막걸리 용량 랜덤, N 개 주문하고 K 명에게 똑같이 나누기
# 하지만 막걸리가 섞이는 게 싫어서 남으면 그냥 버림
# 최대한 많은 양의 막걸리를 분배하는 용량  x ml? -> 이분탐색으로 구하기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
volumes = [int(input()) for _ in range(n)]
# 주전자 <= 사람 수
# 주전자 용량을 x 로 분리해서 사람 수 맞게 분배
# 각 용량을 x로 나눈 몫의 합이 k가 되도록 해야 함
left, right = 1, sum(volumes) // k
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0

    for volume in volumes:
        total += volume // mid

    if total < k:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)