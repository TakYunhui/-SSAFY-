# 실버2. 침투
# 전류가 가장 바깥쪽 흰색 격자에 공급 > 0번째 행에만 공급
# 안쪽까지 침투됨 -> n-1행까지 도달할 수 있느냐 확인
import sys
input = sys.stdin.readline
# 입력값 & 방문 확인 배열
m, n = map(int, input().split())
arr = list(list(map(int, input().strip())) for _ in range(m))
visited =list([0] * n for _ in range(m))
# 좌표 넣기
def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()
        if x == m-1:
            return "YES"

        for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx, ny = x + d[0], y + d[1]
            # 1. nx, ny가 행렬 범위내 2. 다음 위치가 전류가 도달 가능함 3. 방문한 적 없는 곳임
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0 and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1
    return "NO"

result = "NO"
for j in range(n):
    # 1. 현재 arr 내 좌표가 전류가 통하는 칸임(0) 2. 방문한 적이 없어야 함
    if arr[0][j] == 0 and not visited[0][j]:
        result = dfs(0, j)
        if result == "YES":
            print(result)
            # YES인 경우 2번 출력됨을 방지
            exit(0)
print(result)