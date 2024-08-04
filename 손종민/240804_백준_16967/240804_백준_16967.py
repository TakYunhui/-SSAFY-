
import sys
sys.stdin = open('input.txt')

H, W, X, Y = map(int, input().split(' '))
ls = [list(map(int, input().split(' '))) for _ in range(H + X)]
result = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        result[i][j] = ls[i][j]

for i in range(X, H):
    for j in range(Y, W):
        result[i][j] = ls[i][j] - result[i - X][j - Y]

for i in range(H):
    for j in range(W):
        print(result[i][j], end=' ')
    print("")