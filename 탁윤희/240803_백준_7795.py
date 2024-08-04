# 실버 3. 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline

def binary_search(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def count_pairs(a, b):
    count = 0
    for i in a:
        # a 그룹 각 요소에 대한 이분 탐색
        count += binary_search(b, i)
    return count

t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    results.append(count_pairs(a, b))

for result in results:
    print(result)