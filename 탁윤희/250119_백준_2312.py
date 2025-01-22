# 실버3. 수 복원하기
# 소인수분해 결과의 인수와 그 인수 곱해진 횟수
import sys, math
input = sys.stdin.readline

t = int(input())  # 테스트 케이스 수 입력

for _ in range(t):
    n = int(input())  # 각 테스트 케이스에서의 숫자 N 입력
    factors = []  # 소인수와 횟수를 저장할 리스트

    # 소인수분해 진행
    for i in range(2, int(math.sqrt(n)) + 1 ):  # i는 2부터 √N까지
        count = 0  # 현재 인수의 횟수
        while n % i == 0:  # 나눌 수 있는 동안 나눈다
            n //= i
            count += 1
        if count > 0:  # 횟수가 0보다 크면 결과에 추가
            factors.append((i, count))

    # 남은 N이 소수인 경우 처리
    if n > 1:
        factors.append((n, 1))

    # 결과 출력
    for factor, count in factors:
        print(factor, count)
