# 실버1. 강아지는 많을 수록 좋다
from collections import deque
import sys
input = sys.stdin.readline

# 입력
n, m, a, b = map(int, input().split())
closed_intervals = []
for _ in range(m):
    l, r = map(int, input().split())
    closed_intervals.append((l, r))

# 구간 정렬
closed_intervals.sort()

# 방문 배열 및 BFS 초기화
visited = [0] * (n + 1)
q = deque([0])  # 시작점

# BFS
while q:
    x = q.popleft()

    for i in (a, b):  # a 생성 마법, b 생성 마법
        nx = x + i
        if 0 <= nx <= n and not visited[nx]:
            # 닫힌 구간에 포함되지 않는 경우에만 진행
            is_closed = False
            for l, r in closed_intervals:
                if l <= nx <= r:
                    is_closed = True
                    break
            if not is_closed:
                q.append(nx)
                visited[nx] = visited[x] + 1

# 결과 출력
if visited[n] == 0:  # N에 도달할 수 없는 경우
    print(-1)
else:
    print(visited[n])
