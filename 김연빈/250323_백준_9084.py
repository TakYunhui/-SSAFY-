# 동전
T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0]+list(map(int, input().split()))
    M = int(input())
    dp_list = [[0]*(M+2) for _ in range(N+1)] #2d

    for i in range(1, N+1):
        for total in range(1, M+1):
            k = total - coins[i]
            if (k>0):
                dp_list[i][total] = dp_list[i][k] + dp_list[i-1][total]
            elif (k==0):
                dp_list[i][total] = dp_list[i-1][total] + 1
            else:
                dp_list[i][total] = dp_list[i-1][total]
    print(dp_list[N][M])
'''
2 3
0 0 1 2 3 4 5 6 ... 10
0 - 0 0 0 0 0 0
1 - 0 0 0 0 0 0
2 1 0 1 0 1 0 1
3 1 0 1 1 1 1 2

'''