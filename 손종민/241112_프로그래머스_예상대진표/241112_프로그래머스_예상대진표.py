# N을 계속 2로 나누면서
# 범위( 0 ~ N // 2) 안에 두 수가 모두 있는지 확인
# 모두 있으면 카운트하지 않음 (가지 한 단계 올라가지 않음)
# 범위가 다르면 카운트

def solution(n,a,b):
    answer = 0

    while n > 1:
        n /= 2
        if a <= n and b <= n:
            continue
        elif a > n and b > n:
            continue
        else:
            answer += 1

    return answer

n = 8
a = 4
b = 7

print(solution(n, a, b))