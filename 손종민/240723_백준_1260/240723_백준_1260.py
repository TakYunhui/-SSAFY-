import sys

sys.stdin = open('input.txt')

N, M, V = map(int, input().split(' '))

graph = []

# 방문표시 할 리스트
visited = [0] * (N + 1)
now = V
for _ in range(M):
    line = list(map(int, input().split(' ')))
    graph.append(line)

# DFS
result_dfs = []
while visited.count(0) > 1:
    for line in graph:
        if line[0] == now and visited[now] == 0:
            visited[now] = 1
            result_dfs.append(now)
            now = line[1]

print(result_dfs)