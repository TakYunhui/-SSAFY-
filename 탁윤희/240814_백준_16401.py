# 실버 2. 과자 나눠주기
import sys
input = sys.stdin.readline

# 조카 수 m, 과자 수 n
m, n = map(int, input().split())
# 조카들에게 나눠줄 과자의 최대 길이 result 구하기
# 과자를 여러 조각으로 나눌 순 있지만 합칠 순 없다
snacks = list(map(int, input().split()))
left, right = 1, max(snacks)
result = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for snack in snacks:
        if snack >= mid:
            # cnt를 단순 증가 시킬 것이 아니라 mid로 나눈 몫을 넣어서 분리한 과자로 m에 맞출 수 있다
            cnt += snack // mid
    if cnt < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)