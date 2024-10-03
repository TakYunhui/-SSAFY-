def solution(citations):
    answer = 0
    # 내림차순 정렬 후 논문의 순위(인용 많이 받은 수), 각 논문 인용 횟수 비교
    # 조건 성립 안 하면 제외
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            answer = i + 1
    return answer