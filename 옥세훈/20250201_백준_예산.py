# tier gold3 - 73p
# I would like to know about problems-solving point related to silver 2
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
target = int(input())

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= target:
        start = mid + 1
    else:
        end = mid -1


print(end)


