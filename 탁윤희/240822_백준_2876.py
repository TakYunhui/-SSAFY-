# 실버 3. 그래픽스 퀴즈
import sys
input = sys.stdin.readline

n = int(input())
grades = [(0, 0)] # 인덱스를 1부터 사용하기 위해 (0,0) 추가
for _ in range(n):
    a, b = map(int, input().split())
    grades.append((a, b))

dp = [[[0]*2 for _ in range(2)] for _ in range(n+1)]    # 왼쪽 학생, 오른쪽 학생
ans = [0, 5]    # 명수, 그레이드(가장 큰 그레이드를 저장해 최소 그레이드로 갱신할 것)

for i in range(1, n+1):
    for j in range(2):  # i번째 책상의 2명의 학생
        dp[i][j][1] = grades[i][j]   # 그레이드
        for k in range(2):  # i-1번째 책상까지의 누적값 2개
            if grades[i][j] == dp[i-1][k][1]:    # 같은 그레이드를 받은 학생이라면 학생 수 저장
                dp[i][j][0] = dp[i-1][k][0]
                break
        dp[i][j][0] += 1 # 현재 학생을 포함하여 학생 수 증가(업데이트)

        # 최대 학생수와 그레이드 업데이트
        if ans[0] < dp[i][j][0]:
            ans = [dp[i][j][0], dp[i][j][1]]  # 명수, 그레이드
        elif ans[0] == dp[i][j][0] and ans[1] > dp[i][j][1]:
            ans[1] = dp[i][j][1]  # 더 낮은 그레이드로 갱신

print(*ans)