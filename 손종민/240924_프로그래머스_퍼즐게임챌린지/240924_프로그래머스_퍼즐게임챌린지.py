def solution(diffs, times, limit):
    level = 1
    time = 0
    
    while limit:
        # 하나씩 돌리는 동안
        for i in range(len(diffs)):
            # 레벨이 난이도보다 작으면
            if level < diffs[i]:
                if i == 0:
                    time += (diffs[i] - level) * times[i] + times[i]
                else:
                    # cur + prev
                    time += (diffs[i] - level) * (times[i] + times[i - 1])
            else:
                time += times[i]
        
        if time < limit:
            break
        else:
            time = 0
            level += 1
    return level


diffs = [1, 4, 4, 2]
times = [6, 3, 8, 2]
limit = 59

print(solution(diffs, times, limit))