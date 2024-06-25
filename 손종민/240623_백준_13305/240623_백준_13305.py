# 13305 주유소

# N개의 도시, 직선
# 기름 넣고 출발,
# 최소 비용 출력

import sys

sys.stdin = open('input.txt')

# 도시의 갯수
N = int(input())

road = list(map(int, input().split(' ')))
city = list(map(int, input().split(' ')))
# 마지막 도시 기름 가격은 의미가 없다
city.pop()
print(min(city))

oil = 0
cost = 0
latestCourse = sum(road)

# 리스트 순회시키기
# 마지막 도시는 고려할 필요 없으므로
for i in range(N - 1):

    # 도시 가격이 제일 싸다면
    # 남은 코스만큼 다 넣어버리는 게 이득
    if (city[i] == min(city)):
        while oil < latestCourse:
            oil += 1
            cost += city[i]

    # 첫번째 조건에 안 걸리면
    if (oil < road[i]):
        # 기름이 다음 길을 갈 수 있는 기름수보다 적다면
        while oil < road[i]:
            oil += 1
            cost += city[i]
    
    oil -= road[i]
    latestCourse -= road[i]


print(cost)