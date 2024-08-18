from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)


# print(graph)
def bfs():
    q = deque()
    q.append(r)
    visited[r] = True
    cnt = 1

    while q:
        x = q.popleft()
        result[x-1] = cnt
        cnt += 1

        for k in graph[x]:
            if not visited[k]:
                visited[k] = True
                q.append(k)


bfs()

for i in result:
    print(i)
