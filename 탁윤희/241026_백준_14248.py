# 실버2. 점프점프(dfs/bfs)
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())
visited = list(0 for _ in range(n))
def dfs(s):
    # index 맞추기용 -1
    stack = [s-1]
    visited[s-1] = 1
    while stack:
        # 현재 위치한 칸 꺼내기
        jump = stack.pop()

        for d in [1, -1]:
            # 현재 위치 + 점프할 수 있는 거리
            nx = jump + d * arr[jump]

            if 0 <= nx < n and not visited[nx]:
                stack.append(nx)
                visited[nx] = 1
dfs(s)
print(sum(visited))