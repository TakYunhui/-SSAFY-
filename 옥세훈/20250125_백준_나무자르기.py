import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for i in trees:
        if i > mid:
            total += i - mid
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)