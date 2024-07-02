# 1로 만들기

# 할 수 있는 연산
# 3의 배수면 3으로 나누기
# 2의 배수면 2로 나누기
# 1 빼기

# 연산 사용 횟수의 최솟값 출력

# 마지막에 3으로 만들거나 2로 만들어야함 그래야 몫이 1이니까
# 3으로 나눴을때 나머지가 1이면 -1 하고 3으로 나누는게 빠름
# 2로 나눴을때 
# 만약 29라고 생각하면?
# 29 > 28 > 14 > 7 > 6 > 2 > 1
# 29 > 28 > 27 > 9 > 3 > 1
# 음.. 어떻게 해야하지

# 최소 연산횟수 저장하기

N = int(input())
dp = [0] * 10_000_000

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # +1 하는 경우

    if (i % 2 == 0):
        dp[i] = min(dp[i], dp[i//2] +1)
    if (i % 3 == 0):
        dp[i] = min(dp[i], dp[i//3] +1)

print(dp[N])