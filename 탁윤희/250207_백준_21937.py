# 실버 1. 작업
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 인접리스트로 작업관계 표현
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # b를 하려면 a를 해야 하므로 b에 a를 단방향으로 넣음
    graph[b].append(a)

x = int(input()) # 끝낼 작업 x
q = deque([x])
# visited: 탐색 여부 확인 (중복 방지)
visited = [0] * (n+1)
# cnt에 연결된 모든 선행 작업 수를 기록할 것
cnt = 0
while q:
    now = q.popleft()
    for prev in graph[now]:
        if not visited[prev]:
            visited[prev] = 1
            # 연결되어있으면 cnt +1
            cnt += 1
            q.append(prev)
print(cnt)