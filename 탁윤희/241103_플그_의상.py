def solution(clothes):
    answer = 1
    # 1. 딕셔너리 key-value로 종류 별 의상 정리
    categories = dict()
    for cloth in clothes:
        item = cloth[0]
        category = cloth[1]

        if category not in categories:
            categories[category] = []

        categories[category].append(item)

    # 2. 의상 입는 조합 경우의 수 구하기
    # 경우의 수 공식: 종류 n, m이 있으면 (n+1) * (m+1)
    # 위에 -1 해서 아무 것도 안 입는 경우를 빼준다
    print(categories)
    for k, v in categories.items():
        answer *= (len(v) + 1)

    return answer - 1