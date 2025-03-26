# 실버 2. 알고리즘 수업 - 너비 우선 탐색 3
from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
# 양방향 간선 관계를 나타내는 이차원 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (n+1)
q = deque([r])
visited[r] = 0

while q:
    now = q.popleft()
    for next in graph[now]:

        if visited[next] == -1:
            visited[next] = visited[now] + 1
            q.append(next)


for v in visited[1:]:
    print(v)