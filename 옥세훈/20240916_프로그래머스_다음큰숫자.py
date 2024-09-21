def solution(n):
    answer = 0
    num = bin(n)[2:]
    one_cnt = num.count("1")

    while True:
        n += 1
        check_num = bin(n)[2:]
        one_check_cnt = check_num.count("1")
        if one_check_cnt == one_cnt:
            answer = n
            break

    return answer