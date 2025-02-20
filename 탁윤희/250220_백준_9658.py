# 실버 2. 돌 게임 4
n = int(input())
dp = [0] * 1001
# 상근이가 이기는 수를 1로 저장
dp[2], dp[4] = 1, 1

for i in range(5, 1001):
    # 1개, 3개, 4개 이전 수에서 한번이라도 창영(후공)이 이겼다면(==마지막으로 가져간 사람이 상근)
    # 이번 차례에서 상근이가 이길 수 있음
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = 1

print("SK" if dp[n] == 1 else "CY")