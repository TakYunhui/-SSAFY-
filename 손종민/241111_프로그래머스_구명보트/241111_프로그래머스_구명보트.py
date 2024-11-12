def solution(people, limit):
    # 항상 마지막 하나는 남으니 1로 시작
    answer = 0
    people = sorted(people, reverse=True)

    tmp = 0
    for person in people:
        tmp += person
        if tmp > limit:
            answer += 1
            tmp = person
        elif tmp == limit:
            answer += 1
            tmp = 0
        else:
            continue    

    if tmp != 0:
        answer += 1

    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))