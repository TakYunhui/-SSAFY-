from collections import deque
import sys
input = sys.stdin.readline

ni, nj = [0, 1, 0, -1], [1, 0, -1, 0]
n, m, k = map(int, input().split())
arr =[[0] * m for i in range(n)]
check = []
for i in range(k):
  a, b = map(int, input().split())
  arr[a-1][b-1] = 1
  check.append([a, b])

# print(arr)
def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  cnt = 1

  while q:
     i, j = q.popleft()
     for k in range(4):
        xi, xj = i+ni[k], j+nj[k]
        if 0 <= xi < n and 0 <= xj < m and not visited[xi][xj]:
           if arr[xi][xj] == 1:
            visited[xi][xj] = True
            q.append((xi, xj))
            cnt += 1

  return cnt

visited = [[False] * m for i in range(n)]
check_num = 0
for i in check:
    a, b = i
    num = bfs(a-1, b-1)
    if check_num < num:
        check_num = num
      
print(check_num)