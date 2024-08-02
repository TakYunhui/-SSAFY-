# 실버 3. 피보나치 수의 확장
n = int(input())

def fibo(n):
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, (a + b) % 1000000000  # 결과를 절대값으로 1,000,000,000으로 나눈 나머지를 저장
    return a

if n < 0:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
    print(fibo(n))
elif n == 0:
    print(0)
    print(0)
else:
    print(1)
    print(fibo(n))