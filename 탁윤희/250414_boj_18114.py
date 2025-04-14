# 골드 5. 블랙 프라이데이
# c에 맞는 조합 개수 구하기
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# 물건 최대 3개까지 선택하여 c 나오는 개수 구하기
# 물건 3개까지 선택해서 c 나오는 경우 다 구하는 줄 알았음
# 예제1) 1,4 / 2,3 / 5 해서 총 3개라 생각했는데 x
# ㄴ 2/3, 5 해서 1개?
# 그냥 조합이 있으면 바로 print(1) 없으면 (0)이었다!

# 1개로 c가 되는 경우, 바로 출력 후 종료
if c in arr:
    print(1)
    exit()

# 이분탐색 정의
def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

# 2개, 3개 조합
l, r = 0, n-1
while l < r:
    now = arr[l] + arr[r]
    # 2개합이 c면 1출력 후 종료
    if now == c:
        print(1)
        exit()
    # c보다 크면 오른쪽 앞으로 이동시켜서 다시 비교
    elif now > c:
        r -= 1
    # 작으면 1개 추가해서 3개의 합 확인
    else:
        # 이미 있는 2개합을 c에서 빼주고, 그 값을 만족하는 하나의 값이
        # 존재하는지 확인하는 식이다
        if binary_search(l+1, r-1, c-now):
            print(1)
            exit()
        l += 1
print(0)