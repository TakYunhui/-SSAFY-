# 유기농 배추

# 인접해있는 배추들이 몇군데 퍼져있는지

# bfs로 해서 몇번 해야하는지 확인하기?

from collections import deque

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(now_i, now_j):
    # queue
    queue = deque([])
    queue.append((now_i, now_j))
    check[now_i][now_j] = 1

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if (0<=ni<N and 0<=nj<M):
                if (cab_map[ni][nj]==1 and check[ni][nj]==0):
                    check[ni][nj] = 1
                    queue.append((ni, nj))


for tc in range(T):
    M, N, K = map(int, input().split()) # 가로길이, 세로, 배추 수

    cab_map = [[0]*M for _ in range(N)]
    check = [[0]*M for _ in range(N)]
    ans = 0

    for _ in range(K):
        x, y = map(int, input().split())
        cab_map[y][x] = 1
    # print(cab_map)
    
    for i in range(N):
        for j in range(M):
            if (cab_map[i][j]==1 and check[i][j]==0):
                ans += 1
                bfs(i, j)
                
    print(ans)
    for row in check:
        for col in row:
            print(col, end=" ")
        print()