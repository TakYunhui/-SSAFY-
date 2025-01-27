n, k = map(int, input().split())
visited = [False for _ in range(n+1)]
cnt = 0
for i in range(2, n+1):
    if not visited[i]:
        for j in range(i, n+1, i):
            if not visited[j]:
                cnt += 1
                visited[j] = True

            if cnt == k:
                print(j)
                exit()