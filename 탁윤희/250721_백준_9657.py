# 실버 3. 돌 게임
n = int(input())
dp = [1, 1, 0, 1, 1]
for i in range(5, n+1):
    # 첫번째, 세번째, 네번째 돌이 다 상근이어야지 창영이가 win
    if dp[i-1] + dp[i-3] + dp[i-4] == 3:
        dp.append(0)
    else:
        dp.append(1)
if dp[n] == 1:
    print("SK")
else:
    print("CY")
