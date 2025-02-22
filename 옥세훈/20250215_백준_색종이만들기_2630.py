import sys

N = int(input())

domino = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []
def recur(x, y, n):
    color = domino[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != domino[i][j]:
                recur(x, y, n//2)
                recur(x, y+n//2, n//2)
                recur(x+n//2, y, n//2)
                recur(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

recur(0, 0, N)
print(result.count(0))
print(result.count(1))

# 각 범위..
# (0 ~ N//2, 0 ~ N//2), (0 ~ N//2, N//2 ~ N)
# (N//2 ~ N, 0 ~ N//2), (N//2 ~ N, N//2 ~ N)


# 4
# 1 1 0 0
# 1 1 0 0
# 1 0 0 1
# 0 1 1 0
