# 이진법으로 어떻게 바꾸지?


def solution(s):
    answer = [0, 0]

    # s가 1일 때까지 반복
    while s != '1':
        s = list(s)
        answer[1] += s.count('0')
        s = s.count('1')
        s = bin(s)[2:]
        answer[0] += 1
    return answer


s = "01110"

print(solution(s))