n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()
print(arr[0] * n)