def solution(people, limit):
    answer = 0
    # people 한번 정렬 후, 무거운 사람 먼저 넣고 남으면 앞의 가벼운 사람을 한명 더 태운다 (보트 수용 최대 2인!!)
    # 만약 앞의 가벼운 사람 넣는 게 limit 넘어가면 안 태운다
    people.sort()
    # 처음에 pop()을 쓸까 했지만 pop해버리면 아예 빠지므로 변수로 저장해둬야 해서 번거롭다
    # index 포인터 사용한다
    left, right = 0, len(people) - 1
    while left <= right:
        if people[right] + people[left] <= limit:
            left += 1
        # 무거운 사람 1명은 항상 태운다
        right -= 1
        answer += 1

    return answer