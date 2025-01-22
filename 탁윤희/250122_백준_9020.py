# 실버2. 골드바흐의 추측
import sys
input = sys.stdin.readline
# 소수확인
def is_prime(x):
    if x == 1:
        return False
    for j in range(2, int(x ** 0.5) +1):
        if x % j == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    # 가장 차이가 적은 두 소수를 만들기 위해 반으로 쪼개고
    # 하나씩 +1, -1 해보며 두 수가 모두 소수인지 확인
    a, b = n//2, n//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1