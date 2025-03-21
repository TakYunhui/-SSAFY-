# 실버 1. BOJ 거리
# B, O, J 밟으면서 이동
# 번호 증가하는 방향으로 점프: i -> i+1~n까지 점프 가능
n = int(input())
blocks = [0] + list(input())
dp = [int(1e9)] * (n+1)
dp[1] = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        # 조건 따라 B->O, O->J, J->B면 dp 이동하도록 갱신
        # 이때, 최솟값이 들어가도록 기존 수와 대조해가며 갱신
        if blocks[i] == "B" and blocks[j] == "O":
            dp[j] = min(dp[j], dp[i] + (j-i) * (j-i))
        elif blocks[i] == "O" and blocks[j] == "J":
            dp[j] = min(dp[j], dp[i] + (j-i) * (j-i))
        elif blocks[i] == "J" and blocks[j] == "B":
            dp[j] = min(dp[j], dp[i] + (j-i) * (j-i))

if dp[n] == int(1e9):
    print(-1)
else:
    print(dp[n])
