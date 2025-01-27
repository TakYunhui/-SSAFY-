# 실버 2. 소수 부분 문자열
import sys
input = sys.stdin.readline

# 소수 판별 함수
def is_prime(x):
    if x == 1:
        return False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True
#  2 <= x <= 100000 범위 소수 리스트 생성
primes = []
for i in range(2, 100001):
    if is_prime(i):
        primes.append(i)

while True:
    n = input().strip() # 개행 문자 제거
    if n == "0":
        break
    ans = 2
    # 소수가 n에 있다면 ans를 n으로 갱신 -> for문이기에 가장 큰 수가 드가게 됨
    for i in primes:
        if str(i) in n:
            ans = i
    print(ans)