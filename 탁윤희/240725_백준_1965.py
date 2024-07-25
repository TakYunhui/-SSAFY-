# 실버 2. 상자넣기
# 크기 별 상자, 뒤에 있는 상자보다 작은 걸 뒤에 넣을 수 있다
# 방법이 여러 가지
# 한 번에 넣을 수 있는 최대 상자 개수 출력
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))