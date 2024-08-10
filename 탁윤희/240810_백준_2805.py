# 실버 2. 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())), key=lambda x:-x)

# 이분 탐색으로 절단할 높이 h 찾기
left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2
    total = 0
    # 절단되어 얻은 나무 높이 합
    for tree in trees:
        if tree > mid:
            total += tree - mid
        else:
            break

    # 필요 나무 길이 이상이면 절단 높이 높여보기
    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)