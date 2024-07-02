# 동전 0

# 필요한 동전 개수의 최솟값 구하기

N, K = map(int, input().split())

val = list(int(input()) for _ in range(N))

# print(val)

coin = 0

for i in range(N-1, -1, -1):
    if (K // val[i] > 0):
        coin += K//val[i]
        K = K % val[i]

print(coin)
