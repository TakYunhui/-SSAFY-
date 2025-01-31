import sys

k, n = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for i in arr:
        if i >= mid:
            total += (i // mid)

    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)