import sys
sys.setrecursionlimit(10**9) # 재귀 깊이를 늘려줘서 해결
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)
cnt = 1

for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)


# print(graph)
def dfs(v):
    global cnt
    visited[v] = True

    result[v] = cnt
    for k in graph[v]:
        if not visited[k]:
            cnt += 1
            dfs(k)


dfs(r)

for i in result[1:]:
    print(i)