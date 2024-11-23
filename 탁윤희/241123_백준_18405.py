# 골드5. 경쟁적전염
# 모든 바이러스가 1초마다 상하좌우로 증식 -> n * n 보드 안 바이러스 있는 부분에서 동시에 탐색
# 매 초마다 번호가 낮은 종류의 바이러스부터 증식 -> 이해는 되는데 어떤 조건을 넣어야 할 지 잘 모르겠음, 적은 수가 있으면 pass?
# 이미 특정 칸에 바이러스가 있다면 들어갈 수 없음
# n: 판 크기, k: 바이러스 종류 최대 번호, s: s초 후의 값 구함 s까지 탐색시킴? x,y: 해당 위치의 바이러스 번호 구할 것
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
s, x, y = map(int, input().split())

# 바이러스를 동시에 탐색시키기 위해 한 리스트 안에 데이터 저장
# board 자체에 바이러스 증식 기록을 할 수 있어서 visited 삭제됨
virus_data = []
for i in range(n):
        for j in range(n):
            if board[i][j]:
                # 바이러스 번호, 시간, 바이러스 현재 위치 i, j
               virus_data.append((board[i][j], 0, i, j))
# 바이러스 번호 순으로 오름차순 정렬 - 낮은 번호부터 증식시키려고
virus_data.sort()
q = deque(virus_data)

# 방향
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    virus, time, cx, cy = q.popleft()
    # s초가 되면 증식 종료
    if time == s:
        break

    for dx, dy in d:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = virus
            # time을 통해 virus 증식되는 시점 조절 가능
            q.append((virus, time + 1, nx, ny))

print(board[x-1][y-1])