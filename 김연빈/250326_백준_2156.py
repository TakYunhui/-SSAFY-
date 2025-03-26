# 포도주 시식
# 가장 많은 양의 포도주 마실수 있도록

# 계단오르기 같은 dp
N = int(input())
wines = [0]
dp = [0] * (N+1)

for _ in range(N): # 시간 줄이려면 이부분 미리 list 만들어두기
    wines.append(int(input()))

if (N==1):
    print(wines[1])
elif (N==2):
    print(wines[1]+wines[2])
else:
    dp[1] = wines[1]
    dp[2] = dp[1]+wines[2]

    for i in range(3, N+1):
        # 현재X+어제-, 현재O+어제O+그제X+(d-3)-, 현재O+어제X+그제-
        dp[i] = max(dp[i-1], dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i])

    print(max(dp))
    # print(dp)
    # print(wines)

'''
1 2    3       4 5
3 6    1       2 5

3 9 (9,1+3) (9,3+1+2,9+2)

'''
