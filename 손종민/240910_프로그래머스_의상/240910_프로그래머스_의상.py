def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        if cloth[1] not in closet:
            closet[cloth[1]] = 1
        else:
            closet[cloth[1]] += 1
    
    # 튜플로 나오므로 name, cloth로 하여 cloth에 숫자 할당
    for name, cloth in closet.items():
        # print(cloth)
        answer *= (cloth + 1)
    # 경우의 수는
    # 0개 사용 ~ cloth개 사용이므로
    # cloth + 1을 곱해준다

    # print(closet)
    # 아무것도 사용하지 않는 경우 제외
    return answer - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))