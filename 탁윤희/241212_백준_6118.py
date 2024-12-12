from collections import deque
import sys


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 인접 리스트 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs로 리스트 관계 탐색, 1번과 가장 먼 거리를 갖는 것들 모으기
# 개 중 번호가 가장 작은 것 출력!
visited = [-1] * (n+1) # 각 번호 별 거리 저장할 것
q = deque([1])
visited[1] = 0

while q:
    cur = q.popleft()
    for i in graph[cur]:
        if visited[i] == -1:
            visited[i] = visited[cur] + 1
            q.append(i)

number = 1000000000000000000000
max_length = max(visited)
max_cnt = 0
for i in range(1, n+1):
    if visited[i] == max_length:
        number = min(i, number)
        max_cnt += 1
print(number, max_length, max_cnt)
