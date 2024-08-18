from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
di, dj = [1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        i, j = q.popleft()
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = True
                q.append((ni, nj))
                cnt += 1

    if cnt > 0:
        return 1
    return 0

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
          answer += bfs(i, j)

print(answer)
# print(visited)

# 6 6
# 0 0 0 0 0 0
# 1 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0