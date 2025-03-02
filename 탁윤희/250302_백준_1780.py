# 실버 2. 종이의 개수
import sys
input = sys.stdin.readline

n = int(input())
# list()를 map 부분에 감싸고 for _ in range()로 해야 map object가 아니라 이차원 배열로 저장됨
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, z):
    global answer
    visited = arr[x][y]

    for i in range(x, x+z):
        for j in range(y, y+z):
            if arr[i][j] != visited:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1

answer = [0, 0, 0]
dfs(0, 0, n)
[print(res) for res in answer]