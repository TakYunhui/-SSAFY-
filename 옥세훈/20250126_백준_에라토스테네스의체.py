n, k = map(int, input().split())
arr = [i for i in range(2, n+1)]
visit = [False for i in range(n+2)]
cnt = 0
res = 0
p = 0
while cnt < k:

    for i in arr:
        if not visit[i]:
            p = i
            cnt += 1
            res = p
            visit[i] = True
            break

    for j in range(n-1):
        if not visit[arr[j]] and arr[j] % p == 0:
            cnt += 1
            res = arr[j]
            visit[arr[j]] = True

print(res)
