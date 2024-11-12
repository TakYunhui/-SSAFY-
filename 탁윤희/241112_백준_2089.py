# 2089. -2진수
n = int(input())

result = ""
if n == 0:
    print(0)
    exit()
while n:
    # n을 -2로 나눌 때, 나머지가 나오면 result에 1 넣기
    if n % (-2):
        result = "1" + result
        # n을 실제로 -2로 나누고, 이때 나누어 떨어지지 않았으니 1을 더함
        n = n // -2 + 1

    else:
        result = "0" + result
        n //= -2

print(result)