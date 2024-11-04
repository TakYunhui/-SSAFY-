# 1차: bfs로 비어있는 거리 탐색 구현(10분)
# 이 풀이는 최단 거리를 구하지 않고, 모든 빈 자리를 이동하게 한다
# from collections import deque
#
#
# def solution(maps):
#     answer = 100000
#     queue = deque()
#     queue.append((0, 0))
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[0] * m for _ in range(n)]
#
#     while queue:
#         x, y = queue.popleft()
#         for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + d[0], y + d[1]
#
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
#                 visited[nx][ny] = 1
#                 queue.append((nx, ny))
#
#                 if nx == n - 1 and ny == m - 1:
#                     tmp = 0
#                     for i in visited:
#                         print(i)
#                         tmp += i.count(1)
#                     print(visited)
#                     print(tmp)
#
#                     answer = min(tmp, answer)
#
#     if answer == 100000:
#         answer = -1
#
#     return answer

from collections import deque


def solution(maps):
    answer = 100000
    queue = deque()
    queue.append((0, 0))
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    if maps[n - 1][m - 1] == 1:
        return -1

    else:
        return maps[n - 1][m - 1]

# 따로 카운트하는 대신 maps 안에 이동 거리를 저장하니 최단 거리가 나온다
# 왜?
# 1번에서 visited에 방문한 칸 표시하고 이걸 세면 결국 방문한 모든 칸을 세게 된다
# 2번처럼 배열 자체에 이동 거리를 누적하면 큐에 의해 현재까지의 이동 횟수가 기록되는 게 보장되기 때문
# => 매 단계 최단 거리로 다음 칸을 탐색 후 갱신