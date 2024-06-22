# 가장 긴 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))

start = arr[0]
target = arr[0]
ans = [1] * N

# dp인듯 브루트포스인듯?
# 1 <= N, arr <= 1000

for i in range (1, N):
    # 작은 것들 중에 가장 ans가 큰거+1
    maxi = 0
    for j in range(i):
        if arr[j] < arr[i] and maxi < ans[j]:
            maxi = ans[j]
    ans[i] = maxi + 1

print(max(ans))