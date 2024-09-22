def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    first = 0
    end = len(people) - 1

    while first <= end:
        if people[first] + people[end] <= limit:
            end -= 1

        first += 1
        answer += 1

    return answer