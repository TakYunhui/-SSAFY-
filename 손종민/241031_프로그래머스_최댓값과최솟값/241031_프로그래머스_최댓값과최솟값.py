def solution(s):
    ls = list(map(int, s.split(' ')))
    max_num = max(ls)
    min_num = min(ls)
    answer = str(min_num) + ' ' + str(max_num)
    return answer

s = "-1 -2 -3 -4"

print(solution(s))