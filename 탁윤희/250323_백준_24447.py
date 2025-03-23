# 실버 2. 알고리즘 수업 - 너비 우선 탐색 4
from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
# 양방향 간선 정보 저장 이차원 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])
# 방문 여부 체크 배열 (깊이 저장도 동시에)
visited = [-1] * (n+1)
visited[r] = 1
# 방문 순서 체크 배열
cnt = 1
order = [0] * (n+1)
order[r] = cnt

q = deque([r])
visited[r] = 0

while q:
    now = q.popleft()
    # 오름차순 정렬
    visitor = sorted(graph[now])
    for next in visitor:
        # 방문하지 않았다면
        if visited[next] == -1:
            q.append(next)
            visited[next] = visited[now] + 1
            cnt += 1
            order[next] = cnt

result = 0
for i in range(1, n+1):
    result += visited[i] * order[i]
print(result)