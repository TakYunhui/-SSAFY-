import sys

sys.stdin = open('input.txt')

N, D = map(int, input().split(' '))

roads = []
now = 0
result = []
for _ in range(N):
    road = list(map(int, input().split(' ')))
    roads.append(road)

# 현재 위치가 전체 길이보다 작은 동안
while now < D:
    for i in range(N):
        # 길 시작점이 now와 같으면
        if roads[i][0] == now:
            result.append(roads[i])
    now += 1

print(result)