# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
import sys
input = sys.stdin.readline
# 1 = 익은거, 0 = 익지 않은 것, -1 = 없는 것
# m = 행, n = 열
m, n, h = map(int, input().split())
arr = [list(list(map(int, input().split())) for _ in range(n)) for i in range(h)]
# 가장 처음 들어온게 가장 밑에 있음
# visitied를 사용안해도 되는게, 1, 0, -1이 있어서 ㄱㅊ은듯

day = 0
# 동 남 서 북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 위, 아래를 어떻게 전염시켜야 하나..

for i in range(h):
    for j in range(n):
        for k in range(m):
            print(arr[i][j][k])



