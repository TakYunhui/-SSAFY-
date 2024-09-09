# 실버1. 비밀번호
import sys
input = sys.stdin.readline

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 순서
# 비밀번호가 i로 시작할 때 가능한 비번 경우의 수
dp = [[0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# 인접숫자
out = {
    0: [7],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8],
}


t = int(input())
# dp 최댓값 까지 한번에 다 구한 뒤 test case 답 출력
for i in range(2, 1001):
    tmpList = []
    # dp[i][j] = dp[i-1][(인접한 숫자)] 들의 합
    # ex) dp[3][2] = dp[2][1] + dp[2][3] + dp[2][5]
    for j in range(10):
        tmpSum = 0 # 임시 합
        for num in out[j]:
            tmpSum += dp[i-1][num]
        tmpList.append(tmpSum % 1234567)
    dp.append(tmpList)

for _ in range(t):
    print(sum(dp[int(input())]) % 1234567)

