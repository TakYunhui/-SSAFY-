from collections import deque
def solution(maps):
    answer = 0
    di = [1, 0, -1, 0]
    dj = [0, -1, 0, 1]

    max_i = len(maps)
    max_j = len(maps[0])

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            n, m = q.popleft()

            for k in range(4):
                ni, mj = n + di[k], m + dj[k]

                if 0 <= ni < max_i and 0 <= mj < max_j:
                    if maps[ni][mj] == 1:
                        maps[ni][mj] = maps[n][m] + 1
                        q.append((ni, mj))

        return maps[max_i - 1][max_j - 1]

    check = bfs(0, 0)
    if check == 1:
        return -1
    print(check)
    return check

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])