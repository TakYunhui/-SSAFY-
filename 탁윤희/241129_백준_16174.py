# 실버 1. 점프왕 젤리 (large)
from collections import deque
n = int(input())

game = list(list(map(int, input().split())) for _ in range(n))
d = [(0, 1), (1 ,0)]
q = deque([(0,0)])
visited = list([0] * n for _ in range(n))
while q:
    x, y = q.popleft()
    visited[x][y] = 1
    for dx, dy in d:
        nx, ny = x + dx * game[x][y], y + dy * game[x][y]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = 1

if not visited[n-1][n-1]:
    print("Hing")
else:
    print("HaruHaru")