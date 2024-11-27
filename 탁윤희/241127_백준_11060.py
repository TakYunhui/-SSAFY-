# 실버2. 점프 점프
# 1 * n 미로 - 각 칸에 정수가 적힘
# i번째 칸에 쓰인 정수 a 이하만큼 오른쪽으로 점프 가능
# 가장 오른쪽 끝으로 가려면 최소 점프 횟수는?
from collections import deque
n = int(input())

if n == 1:
    print(0)
else:
    maze = list(map(int, input().split()))
    visited = [-1] * (n)
    # dfs 쓴다면 재귀로 각 범위만큼 다 이동시켜서 최소 점프 횟수를 구한다거나?
    # bfs는 그냥 쓰기만 하면 되나? 점프 횟수를 저장시켜서 최후에 비교하기도 해야 할 듯?
    # ㄴ bfs는 각 자리에 도달하는데 걸리는 최소 횟수를 자동 저장하게 될 듯?
    # 가장 초기 값은 제일 왼쪽 인덱스 0을 넣고, 칸 이동에 따라 도달한 인덱스를 넣어가며 탐색해야 함
    # 큐에 초기 인덱스 + 점프 횟수 넣기
    q = deque([(0, 0)])
    while q:
        x, jump = q.popleft()

        for i in range(maze[x]+1):
            nx = x + i

            if nx < n and visited[nx] == -1:
                visited[nx] = jump + 1
                q.append((nx, jump + 1))


    print(visited[-1])