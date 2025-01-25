# 실버1. 소수 사이 수열
# k가 합성수라면 k를 포함하는 소수 사이 수열의 길이 출력
# 소수 수열 찾기 1. 소수 리스트 미리 생성 2. 하나씩 확인
# 테스트 케이스가 여러 개이므로 1의 방법이 효율적일듯?
t = int(input())

# 소수 리스트 생성
def generate_prime(x):
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def is_prime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
# 소수 리스트 미리 생성
max_limit = 1299709
primes = generate_prime(max_limit)
for _ in range(t):
    k = int(input())
    # k가 소수인지 판별 - 소수면 출력 0
    if is_prime(k):
        print("0")
    else:
    # k를 포함하는 소수 사이 수열 길이 찾기
    # k보다 작은 소수 p1과 큰 소수 p2 찾기
        p1, p2 = None, None
        for prime in primes:
            if prime < k:
                p1 = prime
            elif prime > k:
                p2 = prime
                break

        # 결과 출력
        if p1 is not None and p2 is not None:
            print(p2 - p1)
