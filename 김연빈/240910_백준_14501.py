# 퇴사

# N일동안 최대한 많은 상담하기
# 최대 수익 구하기

# DP인것 같음 + 브루트포스
# 상담을 했을 경우, 안했을 경우
# 뒤에서부터 최댓값 구하기? => 왜?

N = int(input())
time = [0] * N
price = [0] * N
dp = [0] * (N+1)
for i in range(N):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

for i in range(N-1, -1, -1):
    if (i+time[i] > N):
        dp[i] = dp[i+1]
    else:
        # 시간에 표시된 칸만큼 건너뛰어서 그거+상담하는경우랑 상담안하는경우 최대값 비교
        dp[i] = max(dp[i+1], dp[i+time[i]]+price[i])

# print(time)
# print(price)
print(dp[0])