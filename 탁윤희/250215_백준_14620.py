# 실버 2. 꽃길
# 3개의 꽃: 화단 밖으로 나가지 않기, 꽃끼리 닿지 않기
# => 4면(0, n-1)을 기준으로 잡지 않기
# 화단 비용: 꽃 모양 기준 5평 -> 가장 싸게 하기
import sys
input = sys.stdin.readline


n = int(input())
prices = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)] # 꽃 심어진 여부 체크 배열
result = int(1e9) # 최소비용 저장

# 방향성(상, 하, 좌, 우)
d = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]

def check(i, j, visited):
    for dx, dy in d:
        x, y = i + dx, j + dy

        if not ((0 <= x < n and 0 <= y < n) and visited[x][y]):
            return False

    return True

def calc(i, j):
    cost = 0
    for dx, dy in d:
        x, y = i + dx, j + dy

        cost += prices[x][y]
    return cost

def dfs(x, cnt, visited, cost_sum):
  global result
  if cnt == 3:
    result = min(result, cost_sum)
    return
  for i in range(x, n-1):
    for j in range(1, n-1):
      if check(i, j, visited):
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
          visited[i + dx][j + dy] = False
        dfs(i, cnt+1, visited, cost_sum + calc(i, j))
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
          visited[i + dx][j + dy] = True

dfs(1, 0, [[True for _ in range(n)] for _ in range(n)], 0)

print(result)
