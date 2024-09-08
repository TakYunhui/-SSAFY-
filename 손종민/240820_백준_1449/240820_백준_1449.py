import sys

sys.stdin = open('input.txt')

N, L = map(int, input().split(' '))
spots = list(map(int, input().split(' ')))

# 1000 이하의 자연수이므로
pipe = [0] * 1000

# 기록 위해 변환
for i in spots:
    pipe[i] = 1


result = 0

for i in spots:
    # L만큼 0으로 바꿔주기
    for j in range(L):
        if i + j < 1000 and pipe[i + j] == 1:
            pipe[i + j] = 0
            result += 1

print(result)