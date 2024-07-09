# 2512 예산
# N개 예산의 합보다 M이 크면
# N 중 최대치 출력
# 합보다 M이 작으면
# M // N 값 출력

import sys

sys.stdin = open('input.txt')
# input = sys.stdin.read()



# # print(requests)

# if M >= sum(requests):
#     print(max(requests))
# else:
#     # 비교를 위한 값
#     tmp = M // N
#     # 순회하면서, tmp 보다 큰 값들 기록
#     # tmp 보다 작으면, 해당값만큼 빼주기
#     count = 0
#     sums = M
#     for i in range(N):
#         if requests[i] > tmp:
#             count += 1
#         else :
#             sums -= requests[i]
    
#     print(sums // count)


N = int(input())
requests = list(map(int, input().split()))
M = int(input())

# 최소, 최댓값 설정
start, end = 0, max(requests)
result = 0

while start <= end:
    # 중간값 설정
    mid = (start + end) // 2
    total_budget = 0

    # 요청받은 예산안 순회하면서
    for i in requests:
        if i > mid:
            total_budget += mid
        else:
            total_budget += i

    # 더한 값이 M보다 작거나 같으면
    if total_budget <= M:
        result = mid
        start = mid + 1
    else:
        # 범위 줄이기
        end = mid - 1
print(result)