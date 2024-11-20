# 실버1. 데스 나이트
from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
# 체스판 구현
board = list([-1] * n for _ in range(n))
# 체스판에서 데스나이트 이동 시키기
def bfs(r, c):
    # 이동방향 directions
    d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    # 시작 위치를 큐에 넣음
    q = deque([(r, c)])
    # r1, c1 초기 위치 방문한 거니까 0 설정
    board[r][c] = 0

    while q:
        x, y = q.popleft()
        for i in range(6):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == -1:
                    board[nx][ny] = board[x][y] + 1
                    q.append((nx, ny))
if r1 == r2 and c1 == c2:
    print(0)
else:
    bfs(r1, c1)
    print(board[r2][c2])
