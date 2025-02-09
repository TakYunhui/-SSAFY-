# 실2. 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global cnt
    visited[node] = cnt
    graph[node].sort()  # 오름차순 정렬
    for next_node in graph[node]:
        if visited[next_node] == 0:
            cnt += 1
            dfs(next_node)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)
cnt = 1
dfs(r) # 시작 정점 탐색

print('\n'.join(map(str, visited[1:])))