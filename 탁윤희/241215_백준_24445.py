# 실버2. 알고리즘 수업 - bfs 2
# 정점, 간선, 시작점
from collections import deque
import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
# 인접 리스트 - 간선 양방향 연결
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
# 내림차순 방문을 위한 정렬
for i in range(n+1):
    graph[i].sort(reverse=True)
# 시작점(r)에서부터 정점 i까지의 방문순서(거리) 출력
q = deque([r])
visited = [0] * (n+1)
visited[r] = 1
cnt = 2
# bfs로 각 정점까지의 거리 visited에 업데이트 --> 순서가 아니네?

while q:
    x = q.popleft()

    for node in graph[x]:
        if not visited[node]:
            visited[node] = cnt
            cnt += 1
            q.append(node)
# 출력
for i in range(1, n+1):
    print(visited[i])