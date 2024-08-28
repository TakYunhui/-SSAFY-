# 실버2. 최대 페이지 수
# 남은 기간 n일과 챕터 수 m개
n, m = map(int, input().split())
data = []
# 챕터 별 소요 일수 & 페이지 수
for i in range(m):
    day, page = map(int, input().split())
    data.append((day, page))

# dp[i]는 i일 동안 읽을 수 있는 최대 페이지 수가 된다
dp = [0 for _ in range(n+1)]

# 챕터를 하나씩 순회하며 dp 테이블 갱신
for day, page in data:
    # 현재 챕터를 사용해 dp 테이블 갱신 (역순)
    # 역순? 현재 챕터가 이미 갱신된 dp 값을 사용하지 않게 함
    for j in range(n, day-1, -1):
        dp[j] = max(dp[j], dp[j-day] + page)

print(dp[n])
