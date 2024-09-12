import sys

input = sys.stdin.readline


def solution(s):
    answer = ''

    s = s.lower()
    s = list(s)

    new_str = []
    check = ""

    for i in s:
        if i == " ":
            if check:
                new_str.append(check.strip())
                check = ""
            new_str.append(" ")
        else:
            check += i

    if check:
        new_str.append(check.strip())

    for i in new_str:
        if i[0].isdigit() and i:
            answer += i
            continue
        if i:
            check = i[0].upper() + i[1:]
            answer += check
        else:
            answer += i

    return answer