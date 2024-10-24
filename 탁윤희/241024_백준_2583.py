# 실버1. 영역 구하기
import sys
input = sys.stdin.readline

# m * n 종이에 k개의 네모 영역을 그린다
m, n, k = map(int, input().split())
# 영역 그릴 모눈종이
paper = list(list(0 for _ in range(n)) for _ in range(m))
# 네모 영역 받기
squares = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append((x1, y1, x2, y2))

# [(0, 2, 4, 4), (1, 1, 2, 5), (4, 0, 6, 2)]
# 1. 종이에 네모 그리기
# 모눈종이 좌표가 (0,0)이 왼쪽 아래, (n,m)이 오른쪽 위
# => y가 아래에서 위로 커지는 형태이므로 y값 변형 필요
# 주어진 y1이 y2보다 아래쪽이지만 파이썬 인덱스는 0부터 m-1까지므로 좌표 뒤집기
for x1, y1, x2, y2 in squares:
    y1, y2 = m - y2, m - y1

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1
# 2. dfs 를 이용하여 그림이 그려지지 않은 영역 cnt + 넓이 구하기
total_cnt = 0
total = []
def dfs(x, y):
    stack = [(x, y)]
    paper[x][y] = 1
    area = 1

    while stack:
        cx, cy = stack.pop()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = cx + dx
            ny = cy + dy
            # nx, ny 범위가 유효한지부터 확인하고 paper visited 여부를 봐야지 index error가 안 남
            if 0 <= nx < m and 0 <= ny < n and not paper[nx][ny] :
                stack.append((nx, ny))
                paper[nx][ny] = 1
                area += 1
    return area
# 외곽 for문이 열, 내부 for문이 행
for x in range(m):
    for y in range(n):
        if not paper[x][y]:
            total.append(dfs(x, y))
            total_cnt += 1
print(total_cnt)
total.sort()
print(*total)