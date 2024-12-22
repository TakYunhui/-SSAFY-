# 실버 1. 1로만들기 2
# 주어진 n에 3가지 연산을 통해 1만들기
# n까지 visited 만들고 연산을 통해 만들어지는 값에 최소 연산 횟수 넣기
from collections import deque

n = int(input())
visited = [-1 for _ in range(n+1)]
prev = [-1 for _ in range(n + 1)]  # 이전 숫자를 저장하는 배열

q = deque([n])
visited[n] = 0

while q:
    x = q.popleft()

    if x == 1:
        print(visited[1])
        # 경로 추적 (1에서 역으로 추적)
        path = []
        while x != -1:
            path.append(x)
            x = prev[x]
        path.reverse()
        print(*path)
        break

    # bfs - 연산 조건을 deque에 넣으면 최소 연산 횟수 보장
    if visited[x//3] == -1 and x % 3 == 0:
        visited[x // 3] = visited[x] + 1
        prev[x // 3] = x  # 이전 숫자 기록
        q.append(x // 3)
    if visited[x//2] == -1 and x % 2 == 0:
        visited[x // 2] = visited[x] + 1
        prev[x // 2] = x  # 이전 숫자 기록
        q.append(x // 2)
    if visited[x-1] == -1 and x - 1 > 0:
        visited[x-1] = visited[x] + 1
        prev[x - 1] = x  # 이전 숫자 기록
        q.append(x - 1)

