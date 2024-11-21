# 실버 2. 아기 상어
# 그래프 탐색 - [-1]로 된 visited 만들고 그 안의 칸 값 갱신
# 갱신기준: 상하좌우대각선 8방향에 1이 없으면 +1, 있으면 저번 값 그대로 넣어주기
# 마지막에 max(visited) 출력
from collections import deque
n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
# bfs 초기설정
visited = list([-1] * m for _ in range(n))
q = deque()
# 방향
d = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# 모든 상어 위치를 q에 넣고 방문 처리
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 0 # 상어 위치의 거리는 0
# bfs 탐색
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m:
            # 상어가 없는 빈칸이면 기존 값 + 1 로 안전거리 갱신
            if visited[nx][ny] == -1:
                  visited[nx][ny] = visited[x][y] + 1
                  q.append((nx,ny))

result = 0
for i in range(n):
    result = max(result, max(visited[i]))
print(result)