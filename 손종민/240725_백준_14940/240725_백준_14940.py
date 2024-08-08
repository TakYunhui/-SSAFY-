import sys
sys.stdin = open('input.txt')

# 세로, 가로
n, m = map(int, input().split(' '))
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split(' '))))

# 2인 지점 찾기
goal = []
for i in range(n):
    for j in range(m):
        if ls[i][j] == 2:
            goal = [i, j]
result = [[0] * m for _ in range(n)]
print(result)
print(goal)