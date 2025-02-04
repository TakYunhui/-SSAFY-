import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

res = 2000000001
x, y = 0, 0

for i in range(n):
    left = 0
    right = (n-1)

    while left <= right:
        mid = (left + right) // 2

        test = arr[mid] + arr[i]

        if test < 0:
            left = mid + 1
        else:
            right = mid - 1

        if abs(test) < abs(res) and mid != i:
            x, y = arr[i], arr[mid]
            res = test

if x > y:
    temp = x
    x = y
    y = temp

print(x, y)
