# 실버2. K 번째 소수
# 25점 풀이 -> 범위 늘리니 시간 초과
# k = int(input())
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def generate_prime(n):
#     primes = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             primes.append(i)
#     return primes
#
# max_limit = 7400000
# primes = generate_prime(max_limit)
#
# print(primes[k-1])

import sys
# 자연수 K를 입력받는다.
N = int(sys.stdin.readline())

# 소수를 구하기 위한 최대 값 (7400000)
M = 7400000

# 소수를 판별하기 위한 배열 생성 (0은 소수, 1은 소수가 아님을 표시)
array = [0] * (M + 1)

# 에라토스테네스의 체를 이용하여 소수를 구한다.
# 2부터 √M까지 순회하면서
for i in range(2, int(M**0.5) + 1):
    # 만약 해당 수가 소수라면
    if array[i] == 0:
        # 그 수의 배수를 모두 소수가 아니라고 표시
        for j in range(i * i, M + 1, i):
            array[j] = 1

# array에서 소수(0으로 표시된 수)를 리스트로 추출
# x에는 모든 소수가 담긴다.
x = [i for i in range(2, M + 1) if array[i] == 0]

# K번째 소수를 출력 (N번째 소수는 리스트의 N-1번째 인덱스에 위치)
print(x[N - 1])
# 출처: https://edder773.tistory.com/155 [개발하는 차리의 학습 일기:티스토리]