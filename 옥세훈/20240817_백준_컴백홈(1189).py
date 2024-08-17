import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

# r-1, 0 => 시작점
# 0, c-1 => 도착점
# T는 못가는 곳
# dfs 로 k 보다 값이 작으면 지나갈 수 있도록..
ni, nj = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [list(input().rstrip())for _ in range(r)]
answer = 0

# print(arr)
def dfs(x, y, dist):
    global answer
    if dist == k and  x == 0 and y == c-1:
        answer += 1
    else:
        arr[x][y] = 'T'
        for i in range(4):
            nx, ny = x + ni[i], y + nj[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
                arr[nx][ny] = 'T'
                dfs(nx, ny, dist + 1)
                arr[nx][ny] = '.'


dfs(r-1,0,1)

print(answer)

