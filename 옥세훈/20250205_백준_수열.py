import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

window = sum(arr[:k])
result = window

for i in range(k, n):
    window += arr[i] - arr[i - k]
    result = max(window, result)

print(result)