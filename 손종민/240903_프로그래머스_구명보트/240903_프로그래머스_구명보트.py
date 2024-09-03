def solution(people, limit):
    answer = 0
    people.sort()
    tmp = [0] * len(people)
    for i in range(len(people)):
        rest = limit
        rest -= people[i]
        if tmp[i] != 1:
            tmp[i] = 1
            answer += 1
        while rest > 0 and i + 1 < len(people):
            i += 1
            if tmp[i] != 1 and people[i] <= rest:
                rest -= people[i]
                tmp[i] = 1

    return answer


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))