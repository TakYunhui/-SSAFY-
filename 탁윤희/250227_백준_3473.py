# 실버3. 교수가 된 현우
# 0의 개수: 10이 몇 번 곱해졌는지를 의미 -> 2 x 5
# 2가 5보다 많이 나오니 5의 개수를 구하면 된다
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    divisor = 5
    while n >= divisor:
        count += n // divisor
        divisor *= 5
    print(count)
