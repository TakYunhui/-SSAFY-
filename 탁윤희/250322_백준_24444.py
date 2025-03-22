# 실버 2. 알고리즘 수업 - 너비 우선 탐색 1
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
# 방문 여부 체크 배열
visited = [0] * (n+1)
visited[r] = 1
# 방문 순서 체크 배열
cnt = 1
order = [0] * (n+1)
order[r] = cnt

while q:
    now = q.popleft()
    # 오름차순 정렬
    visitor = sorted(graph[now])
    for next in visitor:
        # 방문하지 않았다면
        if not visited[next]:
            # 탐색 기록
            q.append(next)
            visited[next] = 1
            # 순서 기록
            cnt += 1
            order[next] = cnt

for i in range(1, n+1):
    print(order[i])