# 풀이참고
# 이전풀이와 동일

import sys

input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = 0

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for child in graph[now]:
            if visited[child] == 0:
                q.append(child)
                visited[child] = 1


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 차례로 가면서 그룹찾기
for i in range(1, N+1):
    if visited[i] == 0:
        ans += 1
        bfs(i)

print(ans)