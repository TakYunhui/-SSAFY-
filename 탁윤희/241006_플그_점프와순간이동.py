def solution(n):
    ans = 0
    # 역순으로 봤을 때, 2로 나누어 떨어지지 않는 순간에 +1 건전지 사용량 발생
    while n:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ans += 1

    return ans