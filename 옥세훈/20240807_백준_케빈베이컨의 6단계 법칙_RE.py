import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start):

    num = [0] * (n+1)
    check[start] = 1

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if check[i] == 0:
                num[i] = num[x] + 1
                check[i] = 1
                q.append(i)

    return sum(num)


n, m = map(int, input().split())
ls = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    ls[a].append(b)
    ls[b].append(a)


result = []
for i in range(1, n+1):
    check = [0] * (n+1)
    result.append(bfs(ls, i))

print(result.index(min(result)) + 1)