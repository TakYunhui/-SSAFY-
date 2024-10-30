# 일단 입력이 문자열이므로 입력 받고 튜플로 바꿔줘야 함.

def solution(s):
    s = s[1:-1].split("},{")
    # print(s)
    new_s = []
    for i in range(len(s)):
        if len(s) == 1:
            # print(s[i][1:-1])
            new_s.append(int(s[i][1:-1]))
            return new_s

        if i == 0:
            new_s.append(tuple(map(int, s[i][1:].split(','))))
        elif i == len(s)-1:
            new_s.append(tuple(map(int, s[i][:-1].split(','))))
        else:
            new_s.append(tuple(map(int, s[i].split(','))))
    
    new_s.sort(key=lambda x: len(x))
    tmp = []
    answer = []
    for item in new_s:
        tmp.extend(item)
    for item in tmp:
        if item not in answer:
            answer.append(item)

    return answer



s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

print(solution(s))