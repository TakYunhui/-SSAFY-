# n이 주어졌을 때
# n // 2까지
# 더해보자


def solution(n):
    answer = 0

    end = n // 2
    num = 1
    # n//2 넘어갈 때까지
    while num <= n:
        # 임시로 할당
        tmp = num
        tmp_sum = 0
        while tmp <= n:
            tmp_sum += tmp
            tmp += 1
            if tmp_sum == n:
                answer += 1
                break
            elif tmp_sum > n:
                break
        num += 1


    return answer


n = 15

print(solution(n))