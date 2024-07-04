# 구간 합 구하기 4

# i번째 수부터 j번째 수까지 합를 구하는 프로그램

# 처음에 처음 ~ 누적합을 다 구해두고 거기서 빼면 될듯? # 시간초과 왜? > pypy로 하니까 됨

N, M = map(int, input().split())

nums = list(map(int, input().split()))

sums = [0] * (N+1) # 1번 숫자 더한건 sums[1]에 저장

for i in range(N):
    sums[i+1] = sums[i] + nums[i]

# print(sums)

for _ in range(M):
    i, j = map(int, input().split())

    print(sums[j] - sums[i-1])
