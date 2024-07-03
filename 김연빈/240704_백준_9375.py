# 패션왕 신해빈

# 알몸이 아닌 상태로 며칠동안 다닐 수 있는가?

# 조합문제인 듯?

T = int(input())

for tc in range(T):
    closet = dict()
    
    N = int(input())
    
    for _ in range(N):
        name, category = input().split()
        dict_cat = closet.get(category)

        if (dict_cat == None):
            closet[category] = 1
        else:
            closet[category] += 1
    
    ans = 1
    for key in closet:
        ans *= closet[key] + 1 # 사용하지 않는 경우 추가
    
    print(ans-1) # 아무것도 입지않는 경우 제외