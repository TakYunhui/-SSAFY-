
def solution(n):
    answer = 0

    def check(check_num):
        cnt = check_num
        while True:
            if check_num == n:
                return 1
            elif check_num > n:
                return 0

            cnt += 1
            check_num += cnt

            # print(check_num, "check_num")


    for i in range(1, n+1):
        # print(i, check(i))
        answer += check(i)

    return answer


print(solution(7))