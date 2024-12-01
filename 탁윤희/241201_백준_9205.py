# 골5. 맥주 마시면서 걸어가기
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input()) # 편의점 개수
    # 집 - 중간 편의점들 - 락페 좌표들
    coordinates = [tuple(map(int, input().split())) for _ in range(n+2)]


    # 좌표 간 차이(x+y)가 1000 넘어가면 sad 아니면 happy
    visited = [0] * (n+2)
    q = deque([0]) # 시작점을 시작 좌표 대신 시작 인덱스 0 으로 변경 (0번 노드)
    while q:
        current = q.popleft()
        x, y = coordinates[current]

        if current == n + 1:
            print("happy")
            break
        # 다른 노드 탐색
        for i in range(n+2):
            # i번 노드 방문하지 않았다면 해당 노드의 좌표 꺼내고 맨해튼 거리 계산
            if not visited[i]:
                nx, ny = coordinates[i]
                # 거리 차가 1000이하면 이동 가능
                if abs(nx - x) + abs(ny - y) <= 1000:
                    visited[i] = 1
                    q.append(i)
    else:
        print("sad")
