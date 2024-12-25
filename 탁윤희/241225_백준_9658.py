# 실버2. 돌 게임 4
n = int(input())
dp = [0] * 1001
# dp[i]가 1일 때 SK 승
dp[2], dp[4] = 1, 1

for i in range(5, 1001):
    # 돌이 1개/3개/4개 중 하나라도 창영이가 지는 상황이라면
    # 상근이는 해당 돌을 가져가 그 상태로 몰아가서 승리할 수 있다.
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = 1

print("SK" if dp[n] else "CY")