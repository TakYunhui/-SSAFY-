# 실버1. 현수막
# bfs나 dfs로 1이 이어진 범위를 탐색하고 1 return
# 최종적으로 return된 1의 개수 count
from collections import deque
import sys

input = sys.stdin.readline


m, n = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(m))
visited = [[0] * n for _ in range(m)]
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and data[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
    # 탐색 끝나면 1 반환
    return  1

result = 0
for i in range(m):
    for j in range(n):
        if data[i][j] and not visited[i][j]:
            result += bfs(i, j)
print(result)
