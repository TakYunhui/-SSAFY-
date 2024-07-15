
import sys

sys.stdin = open('input.txt')

# 굴다리 길이
N = int(input())
# 가로등 갯수
M = int(input())

road = [0] * (N + 1)
lightPositions = list(map(int, input().split()))

height = 0
# 0이 존재하는 동안 계속해서 반복
while road.count(0) > 0:
    # 각 포지션 별로 순회하면서
    # 높이에 따라 해당 포지션 0 채워주기
    height += 1
    for light in lightPositions:
        # print('가로등위치', light)
        # print('가로등 높이', height)
        road[light] = 1
        if light + height <= N:
            road[light + height] = 1
        if light - height >= 0:
            road[light - height] = 1

    # print(road)



print(height)