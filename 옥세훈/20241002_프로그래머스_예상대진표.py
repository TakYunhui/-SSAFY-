def solution(n, a, b):
    answer = 0

    # n / 2 > b - a => 마지막 단계에서 만남
    # n / 2 < b - a => 두가지로 나뉨

    while a != b:

        if b % 2 == 1:
            b = b + 1

        if a % 2 == 1:
            a = a + 1

        b = b // 2
        a = a // 2

        answer += 1
    return answer