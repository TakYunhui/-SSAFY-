# 실버2. 결혼식
# 1번의 친구 - 친구 2단계 친구까지만 초대
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


# 그래프 초기화 (인접 리스트 사용)
graph = [[] for _ in range(n + 1)]  # 학번 1부터 시작하므로 n+1 크기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 친구 관계는 양방향

# 방문 체크
visited = [False] * (n+1)
# 상근이 학번 + 현재 친구 step
q = deque([(1, 0)])
visited[1] = True

result = 0
while q:
    current, step = q.popleft()
    if step == 2:
        continue

    for friend in graph[current]:
        # 이미 방문한 친구면 추가 안 하게 하여 중복 방지
        if not visited[friend]:
            # 현재 사람의 친구, 단계 추가
            visited[friend] = True
            q.append((friend, step + 1))
            result += 1

print(result)