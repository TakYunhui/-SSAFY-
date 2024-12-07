# 실버 3. 에너지드링크
# 2개씩 섞는다 : 1개 베이스 + 1개 2분의 1
n = int(input())
drinks = list(map(int, input().split()))

# 내림차순 정렬
drinks.sort(reverse=True)

# 가장 큰 값을 기준으로 나머지 값을 절반씩 더하기
result = drinks[0]
for drink in drinks[1:]:
    result += drink / 2

print(result)
