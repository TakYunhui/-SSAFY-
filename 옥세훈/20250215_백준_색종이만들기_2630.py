import sys

N = int(input())

domino = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 목표 : 정사각형의 나누는데, 나눈 그 정사각형의 타일들이 0, 1 둘 중 하나로 통일 될 때까지 나누고, 각 1과 0으로만 이루어진 정사각형의 수를 출력하라

# N * N -> N/2 * N/2 -> (N/2)/2 * (N/2)/2
# 귀납법을 생각해보자 도미노 k가 넘어지면 전체가 넘어진다 -> 그럼 k+1도 다 넘어진다. 이 특성을 이용

# zero = 0
# one = 0
def recur(n, arr):
    # 하나의 정사각형이라면 그만.
    if n == 1:
        # 0,1을 구별해야 함.
        return
    # 정사각형 각 타일이 모두 같은 값이라면 그만.
    pass

    check(n)



recur(N, domino)

# N이 8이면 -> 4가 되고, 그럼 각 범위를 구함. 그리고 이를 가지고 다시 -> 2로 나눔, 각 범위를 구함 ->

# 각 범위..
# (0 ~ N//2, 0 ~ N//2), (0 ~ N//2, N//2 ~ N)
# (N//2 ~ N, 0 ~ N//2), (N//2 ~ N, N//2 ~ N)
def check(x):
    for i in range(x//2, x):
        for j in range(x//2, x):
            print(domino[i][j])


# 4
# 1 1 0 0
# 1 1 0 0
# 1 0 0 1
# 0 1 1 0