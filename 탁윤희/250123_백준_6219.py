# 실버 3. 소수의 자격
a, b, d = map(int, input().split())

def is_prime(x):
    if x == 1:
        return False
    for j in range(2, int(x ** 0.5) +1):
        if x % j == 0:
            return False
    return True

cnt = 0
for i in range(a, b+1):
    if str(d) in str(i):
        if is_prime(i):
            cnt += 1
print(cnt)