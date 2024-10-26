# 거꾸로 가면 될 듯?
# n이 홀수인 경우에는 -1하고, count += 1
# n이 짝수라면 n // 2


def solution(n):
    ans = 0
    # n이 0보다 큰 동안
    while n > 0:
        # 짝수면
        if n % 2 == 0:
            n //= 2
        # 홀수면
        else:
            n -= 1
            ans += 1
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return ans


n = 5000

print(solution(n))