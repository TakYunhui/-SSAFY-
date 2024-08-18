from collections import deque
import sys
input = sys.stdin.readline

ni = [0, 1, 0, -1]
nj = [1, 0, -1, 0]
arr = [list(input().split()) for _ in range(5)]


def bfs(i, j):
    q = deque()
    q.append([i, j, ""])

    while q:
        x, y, numbers = q.popleft()
        if len(numbers) == 6:
            if numbers not in result:
                result.append(numbers)
            continue

        for k in range(4):
            nx, ny = x + ni[k], y + nj[k]

            if 0 <= nx < 5 and 0 <= ny < 5:
                q.append([nx, ny, numbers+arr[nx][ny]])

    return numbers


result = []
for i in range(5):
    for j in range(5):
        bfs(i, j)

print(len(result))