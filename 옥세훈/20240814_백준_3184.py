from collections import deque
import sys

input = sys.stdin.readline

ni, nj = [0, 1, 0, -1], [1, 0, -1, 0]

r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
visited = [[False]*c for _ in range(r)]

def bfs(x, y):
    sheep, wolf = 0, 0
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        i, j = q.popleft()
        for k in range(4):
            xi, xj = i+ni[k], j+nj[k]
            if 0 <= xi < r and 0 <= xj < c and not visited[xi][xj]:
                if arr[xi][xj] == '#':
                    continue
                elif arr[xi][xj] == 'o':
                    sheep += 1
                    q.append((xi, xj))
                    visited[xi][xj] = True
                elif arr[xi][xj] == 'v':
                    wolf += 1
                    q.append((xi, xj))
                    visited[xi][xj] = True
                elif arr[xi][xj] == '.':
                    q.append((xi, xj))
                    visited[xi][xj] = True

    if wolf < sheep:
        wolf = 0
        return sheep, wolf

    return 0, wolf


sheep1, wolf1 = 0, 0
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
           a, b = bfs(i, j)
           sheep1 += a
           wolf1 += b

print(sheep1, wolf1)