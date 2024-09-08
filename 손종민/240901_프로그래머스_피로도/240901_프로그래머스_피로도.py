def solution(k, dungeons):
    answer = 0

    dungeons.sort(key=lambda x: (x[1], -x[0]))
    print(dungeons)

    for dungeon in dungeons:
        if k >= dungeon[0]:
            k -= dungeon[1]
            answer += 1
    
    return answer

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution(k, dungeons))