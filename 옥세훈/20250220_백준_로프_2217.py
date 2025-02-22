n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()
mini = arr[0] * n

for i in range(1, n):
    check = arr[i] * (n-i)
    # print(check)
    if check > mini:
        mini = check

print(mini)

# 4
# 2
# 3
# 4
# 100
# ans : 100

# 5
# 1
# 2
# 3
# 4
# 5
# answer : 9
