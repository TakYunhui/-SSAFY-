# 실버2. 너구리 구구
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

# n-1개 줄에 길 정보 입력
for _ in range(n-1):
    a, b, c = map(int, input().split())
    # 양방향 간선 관계 + 거리 추가
    graph[a].append((b,c))
    graph[b].append((a,c))

# 1부터 n-1까지 길 탐색, 가장 긴 거리 저장

visited = [-1] * (n+1)
visited[1] = 0
q = deque([1])

while q:
    current = q.popleft()
    # 인접리스트[current] 인덱스 꺼내어서 다음 관계 번호와 거리 확인
    for next, cost in graph[current]:
        # next 인덱스를 방문하지 않았다면 해당 거리 -- 현재 거리까지의 값 + cost
        # q에 next 번호 추가
        if visited[next] == -1:
            visited[next] = visited[current] + cost
            q.append(next)
print(max(visited))