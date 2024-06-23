import sys

sys.stdin = open('input.txt')

# 도시의 갯수
N = int(input())

# 각 도로의 길이
road = list(map(int, input().split(' ')))

# 각 도시의 주유소 리터당 가격
city = list(map(int, input().split(' ')))

# 초기 비용 및 현재 기름 가격 설정
cost = 0
current_price = city[0]

# 모든 도로를 따라 이동
for i in range(N - 1):
    # 현재 도시에서 다음 도시로 이동하는데 필요한 기름의 비용을 추가
    cost += current_price * road[i]
    
    # 다음 도시의 주유소가 더 저렴하면 가격 갱신
    if city[i + 1] < current_price:
        current_price = city[i + 1]

print(cost)