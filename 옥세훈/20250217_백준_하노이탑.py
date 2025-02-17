N, K = map(int, input().split())

cnt = 0
def recur(a, b, n, num):
    global K, cnt
    if n == 1:
        return
    cnt = num

    recur(a, 6-a-b, n-1, cnt+1)
    if cnt == K:
        print(a, b)
    recur(6-a-b, b, n-1, cnt+1)

recur(1, 3, N, K)