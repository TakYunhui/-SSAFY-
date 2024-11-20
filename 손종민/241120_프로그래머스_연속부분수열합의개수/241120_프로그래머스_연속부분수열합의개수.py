def solution(elements):
    answer = []
    n = 0
    while n < len(elements):
        for i in range(len(elements)):
            this_sum = 0
            cnt = 0
            while cnt <= n:
                if i >= len(elements):
                    i = 0
                this_sum += elements[i]
                i += 1
                cnt += 1 
            answer.append(this_sum)
        n += 1
        set_answer = set(answer)
    return len(set_answer)

elements = [7, 9, 1, 1, 4]
print(solution(elements))