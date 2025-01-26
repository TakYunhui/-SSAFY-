# 실버3. 소수 최소 공배수
n = int(input())
a = list(map(int, input().split()))
def is_prime(x):
    if x == 1:
        return False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True


primes = set()
for num in a:
    if is_prime(num):
        primes.add(num)

if len(primes):
    result = 1
    for prime in primes:
        result *= prime
    print(result)
else:
    print(-1)

