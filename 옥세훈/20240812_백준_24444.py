from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n + 1)
cnt = 1

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1):
  graph[i].sort()

# print(graph)
def bfs():
  global cnt
  q = deque()
  q.append(r)
  visited[r] = 1

  while q:
    x = q.popleft()

    for k in graph[x]:
      if not visited[k]:
        q.append(k)
        cnt += 1
        visited[k] = cnt

bfs()
  
for i in visited:
  print(i)