# 골드 4. 숨바꼭질 2
# bfs 최단 거리 보장
from collections import deque

n, k = map(int, input().split())

visited = [-1] * (100001)
q = deque([n])
visited[n] = 0

cnt = 0


while q:
    x = q.popleft()
    if x == k:
        cnt += 1
        continue

    for nx in x + 1, x -1 , x * 2:
        if 0 <= nx <= 100000:
            if visited[nx] == -1: # 현재 nx 위치에 방문한 적 없다면(처음 도달) 거리+1로 갱신
                visited[nx] = visited[x] + 1
                q.append(nx)
            elif visited[nx] == visited[x] + 1: # 만약 nx 위치에 도달한 적 있지만 동일한 최단 거리로 기록되어있다면
                # 방법의 수를 갱신하기 위해 q에 추가함 (경로의 수를 저장하는 용도!)
                q.append(nx) # nx만 추가

print(visited[k])
print(cnt)