# 실버1. 나무 탈출
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# 인접리스트로 간선 관계(트리) 표현
relations = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

# bfs 풀이
q = deque([1])
visited = [-1] * (n+1)
visited[1] = 0
result = 0

while q:
    now = q.popleft()
    # 현재 노드가 리프 노드(자식 x == 연결된 관계 x 이므로 len 이 1)이면서
    # 1번 노드가 아닌 경우 (!= 1)
    if len(relations[now]) == 1 and now != 1:
        # 현재 노드까지 가기 위한 이동 횟수 더하기
        result += visited[now]
        continue
    # 현재 노드와 연결된 노드(관계) 탐색
    for next in relations[now]:
        if visited[next] == -1:
            # 연결된 노드로 가기 위한 이동 횟수 초기화 선언
            # 현재까지 이동 횟수 + 1 해줘야 next 노드로 도달 가능!
            visited[next] = visited[now] + 1
            q.append(next)

# 성원이가 먼저 시작했기에 결과 값이 홀수여야 우승
if result % 2:
    print("Yes")
else:
    print("No")