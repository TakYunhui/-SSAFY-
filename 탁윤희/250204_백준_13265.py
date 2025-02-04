# 골드 5. 색칠하기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):

    q = deque([x])
    visited[x] = 1 # 색상 1로 시작

    while q:
        now = q.popleft()
        for next in graph[now]:
            # 방문 안 한 노드라면 다른 색 칠하기
            if visited[next] == 0:
                visited[next] = -visited[now]
                q.append(next)
            # 같은 색이 인접하면 이분 그래프 불가
            elif visited[next] == visited[now]:
                return False
    return True

    return True


t = int(input())
for _ in range(t):
    # 동그라미, 직선 개수
    n, m = map(int, input().split())
    # 인접 리스트로 동그라미 연결 관계 표현 (양방향)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # bfs를 통해 2가지 색상으로 표현 가능한지 확인
    # => 서로 연결된 덩어리가 2개까지 나오면 가능, 2개 이상 또는 1개라면 불가능
    result = True
    visited = [0] * (n + 1) # 0: 미방문, 1: 색상1, -1: 색상2
    for i in range(1, n+1):
        if visited[i] == 0: # 방문하지 않은 경우만 bfs 수행
            if not bfs(i):
                result = False
                break

    print("possible" if result else "impossible")


