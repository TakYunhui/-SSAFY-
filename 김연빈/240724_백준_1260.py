# DFS와 BFS

# DFS결과 와 BFS 결과 출력하기
# 번호가 작은것 먼저 방문

from collections import deque

N, M, V = map(int, input().split())

nodes = [[] for _ in range(N+1)]

# 양방향 간선
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for node in nodes:
    node.sort()


visited = [False] * (N+1)
stack = []

def dfs(start): # 재귀 방식. 나중에 stack 방식으로도 풀어보기
    # stack
    # while stack:
        # now = stack.pop()
    now = start
    print(now, end=' ')
    visited[now] = True
    for next in nodes[now]:
        if visited[next] == False:
            dfs(next)


def bfs(start):
    visited = [False] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')
        for next in nodes[now]:
            if visited[next] == False:
                visited[next] = True
                q.append(next)

dfs(V)
print()
bfs(V)