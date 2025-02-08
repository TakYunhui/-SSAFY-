import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

window = sum(arr[:x])
answer = window
period = 1

for i in range(x, n):
    window += arr[i] - arr[i - x]

    if answer == window:
        period += 1

    elif answer < window:
        answer = window
        period = 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(period)

# 5 2
# 1 2 1 2 1
# 3
# 4

# 5 5
# 1 0 0 0 0
# 1
# 1

# 10 2
# 3 0 0 3 0 0 3 0 0 3
# 3
# 6

# 4 2
# 1 2 1 7
# 8
# 1