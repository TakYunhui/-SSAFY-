# 실버2. 역습
import sys
input = sys.stdin.readline

c = int(input())
# 4가지 행동 (긴 패스, 드리블, 패스, 슛) -> 최소 난이도 구하기
# 긴 패스 -> n번째 스트라이커에게 공을 넘김
# 드리블 -> 스트라이커가 공을 계속 가지며 움직임, 횟수 제한 x
# 패스 -> 공을 가진 스트라이커가 바뀜
# 슛 -> 현재 공을 가진 스트라이커만이 놓을 수 있음
for _ in range(c):
    # 이동 지점 개수, 수비수가 스트라이커에게 긴 패스 할 때 난이도 | 스트라이커 슛 난이도
    n, l1, l2, s1, s2 = map(int, input().split())
    # 첫번째 스트라이커 패스 난이도/드리블 난이도
    first_pass = list(map(int, input().split()))
    first_dribble = list(map(int, input().split()))
    # 두번째 스트라이커 패스 난이도/드리블 난이도
    second_pass = list(map(int, input().split()))
    second_dribble = list(map(int, input().split()))
    # 두 스트라이커 별 공을 가진 시점을 비교해야 하므로 2차원 배열의 dp 필요
    dp = [[1001] * n for _ in range(2)]
    dp[0][0] = l1
    dp[1][0] = l2
    for i in range(1, n):
        # 현재 스트라이커가 계속 드리블 | 다른 스트라이커로부터 패스 받은 값
        dp[0][i] = min(dp[0][i-1] + first_dribble[i-1], dp[1][i-1] + second_pass[i-1])
        dp[1][i] = min(dp[1][i-1] + second_dribble[i-1], dp[0][i-1] + first_pass[i-1])

    # 마지막 지점 슛 비용
    result = min(dp[0][-1] + s1, dp[1][-1] + s2)
    print(result)