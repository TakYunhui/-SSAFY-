n = int(input())
stars = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n -3)]
# 윗 변과 밑 변 1 -> 5 -> 9 -> 13 // 4씩 증가
# 왼, 오 변    1 -> 5 -> 9 -> 13
# 중간           1 -> 3 -> 5 -> 7

def recur(num, x, y):
    if num == 1:
        stars[y][x] = '*'
        return

    length = 4 * num - 3

    for i in range(length):
        stars[y][x + i] = '*'
        stars[y + i][x] = '*'
        stars[y + length - 1][x + i] = '*'
        stars[y + i][x + length - 1] = '*'

    recur(num - 1, x + 2, y + 2)

#
recur(n, 0, 0)
for s in stars:
    print(''.join(s))