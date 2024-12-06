# 실버 1. 돌다리
# bfs로 각 숫자 칸에 도달하는 점프 횟수 저장해두기?
from collections import deque
a, b, n, m = map(int, input().split())

q = deque([n])
visited = [-1] * 100001
visited[n] = 0

while q:
    x = q.popleft()

    for i in (1, -1, a, b, -a, -b):
        nx = x + i

        if 0 < nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)

        if i in (a, b):
            nx = x * i
            if 0 < nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)


print(visited[m])
