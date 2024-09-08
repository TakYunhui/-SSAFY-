import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
h1, h2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    q = deque([start])
    visited[start] = True
    num = [0] * (n + 1)

    while q:
        x = q.popleft()
        if x == h2:
            return num[x]
        for k in graph[x]:
            if not visited[k]:
                visited[k] = True
                num[k] = num[x] + 1
                q.append(k)

    return -1

print(bfs(graph, h1))