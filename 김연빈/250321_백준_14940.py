n, m = map(int, input().split())
board = []
answer = [[-1]*m for _ in range(n)]
t_i, t_i = -1, -1
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if (board[i][j]==2):
            t_i, t_j = i, j
            answer[i][j] = 0
            # break
        elif (board[i][j]==0):
            answer[i][j] = 0
    # if (t_i!=-1):
    #     break

#bfs
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
queue = deque()

queue.append((t_i, t_j))
while queue:
    i, j = queue.popleft()
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if (0<=ni<n and 0<=nj<m):
            if (answer[ni][nj]==-1):
                if (board[ni][nj]==1):
                    answer[ni][nj] = answer[i][j]+1
                    queue.append((ni, nj))
                # elif (board[ni][nj]==0):
                #     answer[ni][nj] = 0
# print(answer)
for x in answer:
    for y in x:
        print(y, end=' ')
    print()

'''
2 2
0 0
0 2

이런경우 해결하기 위해서 처음생각했던것처럼 2찾으면서 0 표시하기
'''