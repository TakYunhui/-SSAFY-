def solution(n):
    # 1번 아이디어: n까지의 자연수 배열 생성, n이 되는 연속 숫자 배열 구하기
    # 10000까지 범위니까 시간복잡도가 걸릴 것이다
    # => 수학적 접근
    answer = 0
    for i in range(1, n+1):
        a = (n - (i * (i-1)) // 2) / i
        if a.is_integer() and a > 0:
            answer += 1

    return answer