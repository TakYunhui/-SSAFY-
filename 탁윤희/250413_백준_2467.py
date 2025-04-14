# 골드 5. 용액
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
l, r = 0, n-1
result = [arr[l], arr[r]]
current_sum = int(1e10)
while l < r:
    tmp = arr[l] + arr[r]

    if abs(tmp) < abs(current_sum):
        current_sum = abs(tmp)
        result = [arr[l], arr[r]]
    if tmp < 0:
        l += 1
    else:
        r -= 1
print(*result)