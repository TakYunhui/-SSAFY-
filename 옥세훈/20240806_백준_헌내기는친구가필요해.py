from collections import deque
import sys
input = sys.stdin.readline

ni = [1, 0, -1, 0]
nj = [0, -1, 0, 1]

n, m = map(int, input().split())
ls = []
for i in range(n):
    check = list(map(str, input()))
    ls.append(check)


def bfs(i, j):
    q = deque()
    q.append((i, j))
    ls[i][j] = 1
    answer = 0

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + ni[k], y + nj[k]
            if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] != 1 and ls[nx][ny] != "X":
                if ls[nx][ny] == "P":
                    answer += 1
                ls[nx][ny] = 1
                q.append((nx, ny))

    return answer


x, y = 0, 0
result = 0
found = False
for i in range(n):
    for j in range(m):
        if ls[i][j] == "I":
            x, y = i, j
            break
    if found:
        break

result = bfs(x, y)

if result:
    print(result)
else:
    print("TT")