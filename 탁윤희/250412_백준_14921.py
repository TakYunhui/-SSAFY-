# 골드 5. 용액 합성하기
# 금요일 거랑 유사 유형
import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))

l, r = 0, n-1
result = arr[l] + arr[r]

while l < r:
    # 용액의 차가 아니라 합
    tmp = arr[r] + arr[l]
    # 만약 용액의 합(절댓값)이 result보다 작으면 result 갱신
    if abs(result) > abs(tmp):
        result = tmp
    # 용액 합이 음수면 l 증가, 다음 걸로 바꿈
    if tmp < 0:
        l += 1
    # 용액 합이 양수면 r 감소
    else:
        r -= 1

# 오름차순 정렬된 배열에서 왼, 오 인덱스 값들 더하면 result 확인 가능해짐
print(result)
