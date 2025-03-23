# 동전
T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp_list = [[0]*(M+2) for _ in range(coins[-1]+1)] #2d

    # print(coins)
    # print(dp_list)
    for coin in coins:
        for total in range(1, M+1):
            k = total - coin
            # print(coin, total, k)
            if (k>0):
                dp_list[coin][total] = dp_list[coin][k] + dp_list[coin-1][total]
            elif (k==0):
                dp_list[coin][total] = dp_list[coin-1][total] + 1
            else:
                # print('c')
                dp_list[coin][total] = dp_list[coin-1][total]
                # print('a')
    print(dp_list[coins[-1]][M])
'''
2 3
0 0 1 2 3 4 5 6 ... 10
0 - 0 0 0 0 0 0
1 - 0 0 0 0 0 0
2 1 0 1 0 1 0 1
3 1 0 1 1 1 1 2

'''