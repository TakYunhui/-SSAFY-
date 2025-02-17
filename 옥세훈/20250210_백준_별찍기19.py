n = int(input())
stars = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n -3)]

# 1. 규칙을 찾아냄 (4 * n - 3)
# 2. 2차원 배열을 만들어 각 위치에 찍을 생각을 함

def recur(num, x, y):
    if num == 1:
        stars[x][y] = '*'
        return

    # 재귀 때 마다 바뀌는 길이를 감안함.
    length = 4 * num - 3

    # 밑의 코드부터 이해가 안됨
    for i in range(length):
        stars[x][y + i] = '*' # 윗변
        stars[x + i][y] = '*' # 좌측변
        stars[x + length - 1][y + i] = '*' # 아랫변
        stars[x + i][y + length - 1] = '*' # 우측변

    recur(num - 1, x + 2, y + 2)


recur(n, 0, 0)
for s in stars:
    print(''.join(s))